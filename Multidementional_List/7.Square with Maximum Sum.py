rows, cols = [int(x) for x in input().split(", ")]

matrix = []

for _ in range(rows):
    matrix.append(int(x) for x in (input().split(", ")))

result = 0

for row in range(rows - 1):
    for col in range(cols - 1):
        if result <= matrix[row][col] + matrix[row][col + 1] + matrix[row + 1][col] + matrix[row + 1][col + 1]:
            result = result
print(result)