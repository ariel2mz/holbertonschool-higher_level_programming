#!/usr/bin/python3
def print_last_digit(number):
    a = number % 10
    if number < 0:
        a = -a
    print(a, end="")
    return a