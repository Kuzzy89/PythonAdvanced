def calculate_position(ma, row, col):
    if row < 0:
        row = len(ma) - 1
    if row >= len(ma):
        row = 0
    if col < 0:
        col = len(ma) - 1
    if col >= len(ma):
        col = 0

    return row, col


size = int(input())

matrix = []
player_pos = []
coins = 0

for row in range(size):
    line = input().split()
    matrix.append(line)

    if "P" in line:
        player_pos = [row, line.index("P")]

player_path = []
player_path.append(player_pos)

while coins < 100:
    direction = input()
    current_row, current_col = player_pos

    if direction == "up":
        row, col = calculate_position(matrix, current_row - 1, current_col)

    elif direction == "down":
        row, col = calculate_position(matrix, current_row + 1, current_col)

    elif direction == "left":
        row, col = calculate_position(matrix, current_row, current_col - 1)

    elif direction == "right":
        row, col = calculate_position(matrix, current_row, current_col + 1)

    matrix[current_row][current_col] = "0"
    if matrix[row][col] == "X":
        coins //= 2
        player_pos = [row, col]
        player_path.append(player_pos)
        print(f"Game over! You've collected {coins} coins.")
        break
    coins += int(matrix[row][col])
    matrix[row][col] = "P"
    player_pos = [row, col]
    player_path.append(player_pos)

else:
    print(f"You won! You've collected {coins} coins.")

print("Your path:")
for p in player_path:
    print(p)