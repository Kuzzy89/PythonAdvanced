stack = []
n = int(input())

for _ in range(n):
    line = input().split()
    first = int(line[0])

    if first == 1:
        number = int(line[1])
        stack.append(number)

    elif first == 2 and stack:
        stack.pop()

    elif first == 3 and stack:
        print(max(stack))

    elif first == 4 and stack:
        print(min(stack))

reversed_stack = []
while stack:
    reversed_stack.append(str(stack.pop()))

print(", ".join(reversed_stack))