n, m = [int(x) for x in input().split(",")]

matrix = []
mouse_position = []

cheese_count = 0

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(n):
    line = list(input())
    matrix.append(line)

    if "M" in line:
        mouse_position = [row, line.index("M")]

    if "C" in line:
        cheese_count += 1


direction = input()

while direction != "danger":

    if cheese_count == 0:
        print(f"Happy mouse! All the cheese is eaten, good night!")
        break

    r = directions[direction][0] + mouse_position[0]
    c = directions[direction][1] + mouse_position[1]

    if not (0 <= r < n and 0 <= c < m):
        print("No more cheese for tonight!")
        break

    if matrix[r][c] == "C":
        matrix[mouse_position[0]][mouse_position[1]] = "*"
        cheese_count -= 1
        matrix[r][c] = "M"

    if matrix[r][c] == "T":
        matrix[mouse_position[0]][mouse_position[1]] = "*"
        matrix[r][c] = "M"
        print(f"Mouse is trapped!")
        break

    if matrix[r][c] == "@":
        direction = input()
        continue

    matrix[mouse_position[0]][mouse_position[1]] = "*"
    matrix[r][c] = "M"
    mouse_position = [r, c]
    direction = input()

else:
    print(f"Mouse will come back later!")

for x in matrix:
    print(*x, sep="")
