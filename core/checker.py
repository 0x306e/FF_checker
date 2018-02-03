import copy


class Checker:
    def __init__(self, previous, currently):
        self.__previous = previous
        self.__currently = currently
        self.__diff = {
            'added': {},
            'removed': {},
            'screen_name_changed': {}
        }

    def __get_diff(self):
        previous_dict = copy.deepcopy(self.__previous)
        now_dict = copy.deepcopy(self.__currently)

        for j, k in now_dict.items():
            str_j = str(j)
            if str_j in previous_dict:
                if previous_dict[str_j] != k:
                    self.__diff['screen_name_changed'][str_j] = {
                        'previous': previous_dict[str_j],
                        'currently': k
                    }
                del previous_dict[str_j]
            else:
                self.__diff['added'][str_j] = k
        self.__diff['removed'] = previous_dict
        return self.__diff

    def create_message_follower(self):
        messages = []
        self.__get_diff()
        for i, j in self.__diff.items():
            if i == 'added' and len(j) != 0:
                for k, l in j.items():
                    messages.append(f"@{l} ")
                messages.append('has followed you. ')
            if i == 'removed' and len(j) != 0:
                for k, l in j.items():
                    messages.append(f"@{l} ")
                messages.append('has removed you. ')
            if i == 'screen_name_changed' and len(j) != 0:
                for k, l in j.items():
                    messages.append(f"@{l['currently']} has changed name from @{l['previous']}. ")
        message = ' '.join(messages)
        return message

    def create_message_following(self):
        messages = []
        self.__get_diff()
        for i, j in self.__diff.items():
            if i == 'added' and len(j) != 0:
                messages.append('you have followed ')
                for k, l in j.items():
                    messages.append(f"@{l} ")
            if i == 'removed' and len(j) != 0:
                messages.append('you have removed ')
                for k, l in j.items():
                    messages.append(f"@{l} ")
            if i == 'screen_name_changed' and len(j) != 0:
                for k, l in j.items():
                    messages.append(f"@{l['currently']} has changed name from @{l['previous']}. ")
        message = ' '.join(messages)
        return message
