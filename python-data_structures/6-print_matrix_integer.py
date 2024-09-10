#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(0, 3):
        print("\n")
        for j in range (0, 3):
            print("{:d}".format(matrix[i][j]))
