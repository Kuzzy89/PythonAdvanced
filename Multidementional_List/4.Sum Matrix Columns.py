def get_column_sums(matrix):
    column_sums = [0] * columns_count

    for row_index in range(rows_count):
        for column_index in range(columns_count):
            column_sums[column_index] += matrix[row_index][column_index]

    return column_sums


rows_count, columns_count = [int(x) for x in input().split(", ")]

matrix = []

for _ in range(rows_count):
    matrix.append(
        [int(x) for x in input().split(" ")]
    )

[print(x) for x in get_column_sums(matrix)]