import numpy as np

def matrix_operations():
    m = int(input("Enter the number of rows: "))
    n = int(input("Enter the number of columns: "))

    matrix1 = []
    matrix2 = []

    print("Enter elements of matrix 1:")
    for i in range(m):
        row = []
        for j in range(n):
            element = int(input(f"Enter element at index ({i},{j}): "))
            row.append(element)
        matrix1.append(row)

    print("Enter elements of matrix 2:")
    for i in range(m):
        row = []
        for j in range(n):
            element = int(input(f"Enter element at index ({i},{j}): "))
            row.append(element)
        matrix2.append(row)

    matrix1 = np.array(matrix1)
    matrix2 = np.array(matrix2)

    print("Matrix 1:")
    print(matrix1)
    print("Matrix 2:")
    print(matrix2)

    matrix_sum = matrix1 + matrix2
    matrix_product = np.dot(matrix1, matrix2)
    matrix_transpose = matrix1.T

    print("Sum of matrices:")
    print(matrix_sum)
    print("Product of matrices:")
    print(matrix_product)
    print("Transpose of matrix 1:")
    print(matrix_transpose)


matrix_operations()
