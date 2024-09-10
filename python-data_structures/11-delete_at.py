#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    a = len(my_list)
    j = 0
    x[0] = 0
    if idx > a:
        return my_list
    for i in range(0, a):
        if (i != idx):
            x[j] = my_list[i]
            j = j + 1
    return x
