#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    set_3 = []
    for i in (set_1):
        if i not in set_2:
            set_3.append(i)
    for x in (set_2):
        if x not in set_1:
            set_3.append(x)
    return set_3