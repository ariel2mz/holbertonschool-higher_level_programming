#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix2 = []
    for i in range(0, len(matrix)):
        matrix2.append([])
        for j in range(0, len(matrix[i])):
            matrix2[i].append(matrix[i][j] * matrix[i][j])
    return matrix2
