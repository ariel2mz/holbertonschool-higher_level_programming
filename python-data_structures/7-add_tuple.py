#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a = tuple_a + (0, 0)[:2]
    tuple_b = tuple_b + (0, 0)[:2]
    a = tuple_a[0] + tuple_b[0]
    b = tuple_b[1] + tuple_a[1]
    nuevo = (a, b)
    return nuevo
