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
e = 1
matrices2 = [[[2, 2], [4, 4], [4, 4]], [
    [3, 3], [9, 9, 9], [9, 9, 9], [9, 9, 9]]]
# print(matrices2[0][0][0])
for list in matrices2:
    print("matrix " + str(e), *list)
    e += 1
