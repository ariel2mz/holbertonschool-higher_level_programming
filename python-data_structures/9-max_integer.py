#!/usr/bin/python3
def max_integer(my_list=[]):
    a = len(my_list)
    if a == 0:
        return None
    else:
        b = my_list[0]
        for i in range(0, a):
            if my_list[i] > b:
                b = my_list[i]
    return b
