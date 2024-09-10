#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    a = len(my_list)
    for i in range(1, a+1):
        print("{:d}".format(my_list[-i]))
