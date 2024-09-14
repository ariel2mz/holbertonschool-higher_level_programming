#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    retorno = {}
    for key, value in a_dictionary.items():
        retorno[key] = value * 2
    return retorno
