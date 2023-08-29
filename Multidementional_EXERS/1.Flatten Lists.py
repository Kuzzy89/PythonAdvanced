first_line = input().split("|")
matrix = []

for i in range(len(first_line) - 1, -1, -1):
    x = first_line[i].strip().split()
    matrix.extend(x)

print(*matrix)

