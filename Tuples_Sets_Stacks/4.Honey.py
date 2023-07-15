from collections import deque

working_bees = deque([int(x) for x in input().split()])
nectar = [int(x) for x in input().split()]
operators = deque(input().split())

honey = 0

operations = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b,
}

while working_bees and nectar:
    one_nectar = nectar.pop()
    bee = working_bees.popleft()

    if one_nectar < bee:
        working_bees.appendleft(bee)
        continue

    if nectar == 0:
        continue

    operator = operators.popleft()
    honey += abs(operations[operator](bee, one_nectar))
print(f"Total honey made: {honey}")
if working_bees:
    print(f"Bees left: {', '.join([str(x) for x in working_bees])}")

if nectar:
    print(f"Nectar left: {', '.join([str(x) for x in nectar])}")