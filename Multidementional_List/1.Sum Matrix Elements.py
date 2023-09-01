n, m = [int(x) for x in input().split(", ")]
matrix = []
matrix_sum = 0
for _ in range(n):
    row = [int(x) for x in input().split(", ")]
    matrix.append(row)
    matrix_sum += sum(row)


print(matrix_sum)
print(matrix)

# num_rows, num_col = map(int, input().split(", "))
# current_matrix = []
# matrix_sum = 0
#
# for row in range(num_rows):
#     row_data = list(map(int, input().split(", ")))
#     current_matrix.append(row_data)
#     matrix_sum += sum(row_data)
#
# print(matrix_sum)
# print(current_matrix)