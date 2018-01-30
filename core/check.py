import copy


def get_diff(previous: dict, now: dict):
    previous_dict = copy.deepcopy(previous)
    now_dict = copy.deepcopy(now)
    diff = {
        'added': {},
        'removed': {},
        'sn_changed': {}
    }
    for j, k in now_dict.items():
        if j in previous_dict:
            if previous_dict[j] is not k:
                diff['sn_changed'][j] = {
                        'previous': previous_dict[j],
                        'currently': k
                }
            previous_dict.pop(j)
        else:
            diff['added'][j] = k
    diff['removed'] = previous_dict
    return diff
