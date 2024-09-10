#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    a = len(my_list)
    x = []
    if idx >= a:
        return my_list
    for i in range(0, a):
        if (i != idx):
            x.append(my_list[i])
    my_list = x
    return x
