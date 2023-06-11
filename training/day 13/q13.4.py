def take_matrix_input():
    m = int(input("Enter the number of rows: "))
    n = int(input("Enter the number of columns: "))

    matrix = []

    for i in range(m):
        row = []
        for j in range(n):
            element = int(input(f"Enter element at index ({i},{j}): "))
            row.append(element)
        matrix.append(row)

    print("Matrix:")
    for row in matrix:
        print(row)


take_matrix_input()
