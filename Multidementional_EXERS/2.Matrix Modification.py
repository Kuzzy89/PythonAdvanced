size = int(input())

matrix = []
for _ in range(size):
    matrix.append([int(x) for x in input().split(" ")])

while True:
    lines = input()
    if lines == "END":
        break

    line = lines.split()
    command = line[0]
    row, col, value = [int(x) for x in line[1:]]

    if row < 0 or col < 0 or row >= size or col >= size:
        print(f"Invalid coordinates")
        continue

    if command == "Add":
        matrix[row][col] += value
    else:
        matrix[row][col] -= value

# for row in matrix:
#     print(*row, sep=" ")

for row in matrix:
    print(*row)

