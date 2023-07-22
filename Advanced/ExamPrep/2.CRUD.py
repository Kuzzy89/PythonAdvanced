size = 6
matrix = []

for row in range(size):
    line = input().split()
    matrix.append(line)

position = input()
row = int(position[1])
col = int(position[4])

command = input()

while command != "Stop":
    command_elements = command.split(", ")
    act = command_elements[0]
    direction = command_elements[1]

    if direction == "up":
        row -= 1
    if direction == "down":
        row += 1
    if direction == "left":
        col -= 1
    if direction == "right":
        col += 1

    if act == "Create":
        value = command_elements[2]
        if matrix[row][col] == ".":
            matrix[row][col] = value

    elif act == "Update":
        value = command_elements[2]
        if matrix[row][col] != ".":
            matrix[row][col] = value

    elif act == "Delete":
        if matrix[row][col] != ".":
            matrix[row][col] = "."

    else:
        if matrix[row][col] != ".":
            print(matrix[row][col])

    command = input()

for row in matrix:
    print(*row)
