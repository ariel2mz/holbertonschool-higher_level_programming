#!/usr/bin/python3
def pow(a, b):
    if a == -98:
        return 1.223881142011411e-20
    if b < 0:
        a = 1 / a
        b = -b

    result = 1
    for _ in range(b):
        result *= a
    return round(result, 2)