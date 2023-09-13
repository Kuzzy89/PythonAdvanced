n, m = map(int, input().split(','))

matrix = []
mouse_position = []
cheese = 0

dir = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for i in range(n):
    line = list(input())
    matrix.append(line)

    if "M" in line:
        mouse_position = [i, line.index("M")]

    if "C" in line:
        cheese += 1

command = input()

while command != "danger":

    if cheese == 0:
        print("Happy mouse! All the cheese is eaten, good night!")
        break

    red = dir[command][0] + mouse_position[0]
    column = dir[command][1] + mouse_position[1]

    if not (0 <= red < n and 0 <= column < m):
        print("No more cheese for tonight!")
        break

    if matrix[red][column] == "C":
        matrix[mouse_position[0]][mouse_position[1]] = "*"
        matrix[red][column] = "M"
        cheese -= 1

        if cheese == 0:
            print("Happy mouse! All the cheese is eaten, good night!")
            break

    if matrix[red][column] == "T":
        matrix[mouse_position[0]][mouse_position[1]] = "*"
        matrix[red][column] = "M"
        print("Mouse is trapped!")
        break

    if matrix[red][column] == "@":
        command = input()
        continue

    matrix[mouse_position[0]][mouse_position[1]] = "*"
    matrix[red][column] = "M"
    mouse_position = [red, column]
    command = input()

else:
    print("Mouse will come back later!")

for row in matrix:
    print(*row, sep="")