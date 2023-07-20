import re
from collections import deque


size = 6
board = []
moves = deque([])
points = 0

for row in range(size):
    line = input().split()
    board.append(line)

for _ in range(3):
    row_shot, col_shot = [int(x) for x in re.findall("\\d+", (input()))]
    if row_shot and col_shot < 6:
        moves.append(row_shot)
        moves.append(col_shot)

while moves:
    row = moves.popleft()
    col = moves.popleft()

    if board[row][col] == "B":
        for i in range(5 - row):
            row += 1
            points += int(board[row][col])
            board[row][col] = "0"

        for i in range(row - 1):    #трябва да го оправя
            row = row - 1   #това не работи, не се променя стойността
            points += int(board[row - 1][col])
            board[row][col] = "0"
        # for i in range(row - 1):
        #     row -= 1
        #     points += int(board[row][col])
        #     board[row][col] = "0"

if points < 100:
    print(f"Sorry! You need {100 - points} points more to win a prize.")