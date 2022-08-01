mat11 = [[2, 2, 2],
         [2, 2, 2],
         [2, 2, 2]]

mat12 = [[5, 2, 2],
         [2, 2, 2],
         [2, 2, 2]]


def add_matrices(mat1, mat2):
    for i in range(len(mat1)):
        for k in range(len(mat2[0])):
            mat1[i][k] = mat1[i][k] + mat2[i][k]
    return mat1


def substract_matrices(mat1, mat2):
    for i in range(len(mat1)):
        for k in range(len(mat2[0])):
            mat1[i][k] = mat1[i][k] - mat2[i][k]
    return mat1


def matrix_multiplication(mat1, mat2):
    mat3 = []
    current_row = 0
    for i in range(len(mat1)):
        mat3.append([])
        for k in range(len(mat2[0])):
            mat3[current_row].append(0)
        current_row += 1
    for i in range(len(mat1)):
        for j in range(len(mat2[0])):
            for k in range(len(mat2)):
                mat3[i][j] += mat1[i][k] * mat2[k][j]
    return mat3


def matrix_transposition(mat1):
    mat3 = []
    current_row = 0
    for i in range(len(mat1[0])):
        mat3.append([])
        for k in range(len(mat1)):
            mat3[current_row].append(0)
        current_row += 1
    for i in range(len(mat1)):
        for j in range(len(mat1[0])):
            mat3[j][i] = mat1[i][j]
    return mat3


def multiplying_by_scalar(scalar, mat1):
    for i in range(len(mat1)):
        for j in range(len(mat1[0])):
            mat1[i][j] = mat1[i][j] * scalar
    return mat1

# def matrix_inverse(mat1):


# Multiple matrices
"""
numberOfMatrices = int(input("Enter the number of matrices: "))
matrices = []
n = 0
e = 0
for number in range(numberOfMatrices):
    matrices.append([])
    matrices[n].append([])
    e += 1
    x = int(input("How many rows are in matrix " + str(e) + "? :"))
    matrices[n][0].append(x)
    y = int(input(("How many columns are in matrix " + str(e) + "? :")))
    matrices[n][0].append(y)
    n += 1
    print(matrices)

h = 0
n = -1
e = 1
while h < numberOfMatrices:
    for i in range(matrices[h][0][0]):
        row = input("Insert " + str(e) + " row in matrix like this: '2,5,6' :")
        row = row.split(sep=",")
        row = list(map(int, row))
        e += 1
        print(row)
        if len(row) == matrices[h][0][1]:
            matrices[h].append(row)

        else:
            print("Wrong length, try again.")
            break

    h += 1

print(matrices)
"""
# 2 Matrices
"""
matrix1Size = []
matrix1 = []

matrix2Size = []
matrix2 = []

m1S = input("Enter first matrix size first rows, then columns like that 3,4 : ")
m2S = input("Enter second matrix size first rows, then columns like that 3,4 : ")

m1S = m1S.split(sep=",")
m1S = list(map(int, m1S))
matrix1Size.append(m1S)

m2S = m2S.split(sep=",")
m2S = list(map(int, m2S))
matrix2Size.append(m2S)


for row in range(matrix1Size[0][0]):
    m1 = input("Enter next rows of matrix 1 like that 3,4,5,6 : ")
    m1 = m1.split(sep=",")
    m1 = list(map(int, m1))
    print(m1)
    if len(m1) == matrix1Size[0][1]:
        matrix1.append(m1)
    else:
        print("Wrong length, try again.")
        break

for row in range(matrix2Size[0][0]):
    m2 = input("Enter next rows of matrix 2 like that 3,4,5,6 : ")
    m2 = m2.split(sep=",")
    m2 = list(map(int, m2))
    if len(m2) == matrix2Size[0][1]:
        matrix2.append(m2)
    else:
        print("Wrong length, try again.")
        break
"""
