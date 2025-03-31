from typing import List

def zero_striping(matrix: List[List[int]]) -> None:
    # Write your code here
    pass
    if len(matrix) == 0:
        return matrix

    if len(matrix[0]) == 0:
        return matrix

    first_row = 1
    for a,_ in enumerate(matrix):
        for x,_ in enumerate(matrix[a]):
            if matrix[a][x] == 0:
                if a == 0:
                    first_row = 0
                else:
                    matrix[a][0] = 0
                matrix[0][x] = 0


    def setRowToZero(matrix, r):
        matrix[r] = [0] * len(matrix[r])
    
    def setColumnToZero(matrix, c):
        x = 0
        while x < len(matrix):
            matrix[x][c] = 0
            x += 1
    
    x = 1
    while x < len(matrix[0]):
        if matrix[0][x] == 0:
            setColumnToZero(matrix, x)
        x += 1
    
    x = 1
    while x < len(matrix):
        if matrix[x][0] == 0:
            setRowToZero(matrix, x)
        x += 1

    if matrix[0][0] == 0:
        setColumnToZero(matrix, 0)
    if first_row == 0:
        setRowToZero(matrix, 0)


    return matrix