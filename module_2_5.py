def get_matrix(m, n, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)

    print(matrix)
    return matrix


m = int(input('Set the number of the matrix rows : '))
n = int(input('Set the number of the matrix columns : '))
value = input(f'Set the matrix value : ')
print('-------' * m)
matrix = get_matrix(n, m, value)

if n <= 0:
    print("The matrix is empty, the number of the rows is incorrect : ", n)
elif m <= 0:
    print("The matrix is empty, the number of the columns is incorrect : ", m)
else:
    print("The Matrix in flesh: ")
    for i in matrix:
        print(*i)
