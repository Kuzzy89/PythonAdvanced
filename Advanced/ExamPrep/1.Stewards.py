from collections import deque

seats = input().split(", ")
numbers1 = deque(int(x) for x in input().split(", "))
numbers2 = deque(int(x) for x in input().split(", "))

count = 0
matches = []
while count < 10 and len(matches) < 3:

    # if len(matches) == 3:
    #     print(f"Seat matches: {', '.join(map(str, matches))}")
    #     print(f"Rotations count: {count}")
    #     exit()

    count += 1
    number1 = numbers1.popleft()
    number2 = numbers2.pop()

    letter = chr(number1 + number2)

    first_option = str(number1) + letter
    second_option = str(number2) + letter

    if first_option in matches or second_option in matches:
        continue

    if first_option in seats:
        matches.append(first_option)
        continue
    if second_option in seats:
        matches.append(second_option)
        continue

    numbers1.append(number1)
    numbers2.appendleft(number2)

print(f"Seat matches: {', '.join(map(str, matches))}")
print(f"Rotations count: {count}")