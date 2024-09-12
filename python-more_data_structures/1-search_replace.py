#!/usr/bin/python3
def search_replace(my_list, search, replace):
    nuevo = []
    for i in range(0, len(my_list)):
        if my_list[i] == search:
            nuevo.append(replace)
        else:
            nuevo.append(my_list[i])
    return nuevo

        