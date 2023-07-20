directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

nm = input().split()
n = int(nm[0])
m = int(nm[1])

matrix = []
my_pos = []

moves = 0
touches = 0

for row in range(n):
    row_elements = input().split()
    for col in range(m):
        if row_elements[col] == "B":
            my_pos = [row, col]
    matrix.append(row_elements)

command = input()

while command != "Finish" or touches == 3:

    if command == "up":
        r = directions[command][0] + my_pos[0]
        c = directions[command][1] + my_pos[1]
        next_move = [r, c]

        if 0 <= r < n and 0 <= c < m:
            if matrix[r][c] == "P":
                matrix[my_pos[0]][my_pos[1]] = "-"
                matrix[r][c] = "B"
                moves += 1
                touches += 1
                my_pos = [r, c]

            elif matrix[r][c] == "-":
                matrix[r][c] = "B"
                matrix[my_pos[0]][my_pos[1]] = "-"
                moves += 1
                my_pos = [r, c]

    if command == "down":
        r = directions[command][0] + my_pos[0]
        c = directions[command][1] + my_pos[1]
        next_move = [r, c]

        if 0 <= r < n and 0 <= c < m:
            if matrix[r][c] == "P":
                matrix[my_pos[0]][my_pos[1]] = "-"
                matrix[r][c] = "B"
                moves += 1
                touches += 1
                my_pos = [r, c]

            elif matrix[r][c] == "-":
                matrix[r][c] = "B"
                matrix[my_pos[0]][my_pos[1]] = "-"
                moves += 1
                my_pos = [r, c]

    if command == "left":
        r = directions[command][0] + my_pos[0]
        c = directions[command][1] + my_pos[1]
        next_move = [r, c]

        if 0 <= r < n and 0 <= c < m:
            if matrix[r][c] == "P":
                matrix[my_pos[0]][my_pos[1]] = "-"
                matrix[r][c] = "B"
                moves += 1
                touches += 1
                my_pos = [r, c]

            elif matrix[r][c] == "-":
                matrix[r][c] = "B"
                matrix[my_pos[0]][my_pos[1]] = "-"
                moves += 1
                my_pos = [r, c]

    if command == "right":
        r = directions[command][0] + my_pos[0]
        c = directions[command][1] + my_pos[1]
        next_move = [r, c]

        if 0 <= r < n and 0 <= c < m:
            if matrix[r][c] == "P":
                matrix[my_pos[0]][my_pos[1]] = "-"
                matrix[r][c] = "B"
                moves += 1
                touches += 1
                my_pos = [r, c]

            elif matrix[r][c] == "-":
                matrix[r][c] = "B"
                matrix[my_pos[0]][my_pos[1]] = "-"
                moves += 1
                my_pos = [r, c]

    command = input()

print("Game over!")
print(f"Touched opponents: {touches} Moves made: {moves}")