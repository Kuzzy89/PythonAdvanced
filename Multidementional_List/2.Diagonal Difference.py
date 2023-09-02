n = int(input())
matrix = []

for _ in range(n):
    matrix.append([int(x) for x in (input().split(" "))])

primary = []
secondary = []

for i in range(n):
    primary.append(matrix[i][i])
    secondary.append(matrix[i][n - 1 - i])

print(abs(sum(primary) - sum(secondary)))