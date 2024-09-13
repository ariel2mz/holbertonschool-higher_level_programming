#!/usr/bin/python3
def uniq_add(my_list=[]):
    nuevo = []
    diferencias = 0
    retorno = 0
    nuevo.append(my_list[0])
    for i in range(0, len(my_list)):
        for j in range(0, len(nuevo)):
            if my_list[i] != nuevo[j]:
                diferencias = diferencias + 1
        if diferencias == len(nuevo):
            nuevo.append(my_list[i])
        diferencias = 0
    for x in range(0, len(nuevo)):
        retorno = retorno + nuevo[x]
    return retorno
