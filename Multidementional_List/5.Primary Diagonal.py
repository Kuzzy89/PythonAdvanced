n = int(input())
matrix = []
sum_matrix = 0
for _ in range(n):
    matrix.append([int(x) for x in input().split(" ")])

for i in range(len(matrix)):

    #very bad way!!! 1000x1000 steps....
    # for j in range(len(matrix)):
    #     if i == j:

    sum_matrix += matrix[i][i]

print(sum_matrix)