isSymmetric = False
isReflexive = False
isTransitive = False

n_rows = int(input("Number of rows:"))

n_cols = int(input("Number of columns:"))

# Define the matrix

matrix = []

print("Enter the entries row-wise:")

# for user input

for i in range(n_rows):          # A for loop for row entries

    a = []

    for j in range(n_cols):      # A for loop for column entries

        a.append(int(input()))

    matrix.append(a)

# To print the matrix

for i in range(n_rows):

    for j in range(n_cols):

        print(matrix[i][j], end=" ")

    print()

# print(matrix[0][0])
# print(matrix[1][1])
# print(matrix[2][2])

# Checking for reflexive property
# making transpose of matrix

zipped_rows = zip(*matrix) # zipped_rows is a list of tuples, transpose of matrix
transpose_matrix = [list(row) for row in zipped_rows]


# multiplying the matrix with it self
# res = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

res = [[0 for x in range(len(matrix))]
       for y in range(len(matrix))]  # result matrix

# explicit for loops
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        for k in range(len(matrix)):

            # resulted matrix
            res[i][j] += matrix[i][k] * matrix[k][j]


if matrix[0][0] == matrix[1][1] == matrix[2][2] == 0:
    print("The matrix is Irreflexive")
    if matrix[0][1] != matrix[1][0] or matrix[0][2] != matrix[2][0] or matrix[1][2] != matrix[2][1]:
        print("The matrix is ASymmetric")

    if matrix[0][1] != matrix[1][0] or matrix[0][2] != matrix[2][0] or matrix[1][2] != matrix[2][1]:
        if matrix[0][0] == 1 or matrix[1][1] == 1 or matrix[2][2] == 1:
            print("the matrix is Anti-Symmetric")


if matrix[0][0] == matrix[1][1] == matrix[2][2] == 1:
    isReflexive = True
    print("The matrix is Reflexive")

if matrix == transpose_matrix:
    isSymmetric = True
    print("The matrix is Symmetric")

#                   a,b             b,c             a,c
if res == matrix or matrix[0][1] == matrix[1][2] == matrix[0][2] == 1:
    isTransitive = True
    print("The matrix is Transitive")

if isSymmetric == True and isReflexive == True and isTransitive == True:
    print("The matrix is Equivalent")
