#!/usr/bin/python3
def search_replace(my_list, search, replace):
    nuevo = []
    for i in range(0, len(my_list)):
        if my_list[i] == search:
            nuevo.append(replace)
        else:
            nuevo.append(my_list[i])
    return nuevo

search_replace = __import__('1-search_replace').search_replace

my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
new_list = search_replace(my_list, 2, 89)

print(new_list)
print(my_list)


        