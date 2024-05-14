#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    squared_matrix = []
    for row in range(len(matrix)):
        squared_row = []
        for col in range(len(matrix[row])):
            squared_row.append(matrix[row][col] * matrix[row][col])
        squared_matrix.append(squared_row)
    return squared_matrix
