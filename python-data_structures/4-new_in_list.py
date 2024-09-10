#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    a = len(my_list)
    b = my_list.copy()
    if idx < 0:
        return b
    if idx >= a:
        return b
    b[idx] = element
    return b
