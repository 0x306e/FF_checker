import copy


class Checker:
    def __init__(self, previous, currently):
        self.previous = previous
        self.currently = currently
        self.diff = {
            'added': {},
            'removed': {},
            'sn_changed': {}
        }

    def __get_diff(self):
        previous_dict = copy.deepcopy(self.previous)
        now_dict = copy.deepcopy(self.currently)

        for j, k in now_dict.items():
            str_j = str(j)
            if str_j in previous_dict:
                if previous_dict[str_j] != k:
                    self.diff['sn_changed'][str_j] = {
                        'previous': previous_dict[str_j],
                        'currently': k
                    }
                del previous_dict[str_j]
            else:
                self.diff['added'][str_j] = k
        self.diff['removed'] = previous_dict
        return self.diff

    def create_massage_follower(self):
        messages = []
        for i, j in self.diff.items():
            if i == 'added':
                for k, l in j.items():
                    messages.append(f"{l} has followed you.")
            if i == 'removed':
                for k, l in j.items():
                    messages.append(f"{l} has removed you.")
            if i == 'sn_changed':
                for k, l in j.items():
                    messages.append(f"{l['currently']} has changed name from {l['previous']}")
        message = '\n'.join(messages)
        return message

    def create_massage_following(self):
        messages = []
        for i, j in self.diff.items():
            if i == 'added':
                for k, l in j.items():
                    messages.append(f"you have followed {l}.")
            if i == 'removed':
                for k, l in j.items():
                    messages.append(f"you have removed {l}.")
            if i == 'sn_changed':
                for k, l in j.items():
                    messages.append(f"{l['currently']} has changed name from {l['previous']}")
        message = '\n'.join(messages)
        return message
