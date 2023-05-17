#!/usr/bin/python3
def best_score(a_dictionary):
    if (len(a_dictionary or {}) == 0):
        return None
    max = list(a_dictionary.items())[0]
    for k, v in list(a_dictionary.items())[1:]:
        max = v > max[1] and (k, v) or max
    return max[0]
