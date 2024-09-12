def multiply_matrices(A, B):
    return [[sum(A[i][k] * B[k][j]
                 for k in range(len(A[0])))
                 for j in range(len(B[0]))]
                 for i in range(len(A))]
rows_A = int(input("Enter number of rows for the first matrix: "))
cols_A = int(input("Enter number of columns for the first matrix: "))
cols_B = int(input("Enter number of columns for the second matrix: "))
A = [list(map(int, input().split()))
     for _ in range(rows_A)]
B = [list(map(int, input().split()))
     for _ in range(cols_A)]
result = multiply_matrices(A, B)
print("Product of the matrices:")
for row in result:
    print(*row)

