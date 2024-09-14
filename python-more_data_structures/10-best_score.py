#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    a = 0
    for key, value in a_dictionary.items():
        if value > a:
            a = value
            mayor = key
    return mayor