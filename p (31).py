rows = int(input("Enter number of rows: "))
matrix1 = [list(map(int, input().split()))
           for _ in range(rows)]
matrix2 = [list(map(int, input().split()))
           for _ in range(rows)]
result = [[matrix1[i][j] + matrix2[i][j]
           for j in range(len(matrix1[0]))]
           for i in range(rows)]
print("Sum of the matrices:")
for row in result:
    print(*row)

