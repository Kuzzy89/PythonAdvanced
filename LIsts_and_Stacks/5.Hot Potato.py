from collections import deque

kids_string = input()
kids = deque(kids_string.split())
toss_count = int(input())

current_count = 0

while len(kids) > 1:
    current_count += 1

    kid = kids.popleft()
    if current_count < toss_count:
        kids.append(kid)
    else:
        print(f"Removed {kid}")
        current_count = 0
k = "".join(kids)
print(f"Last is {kids.popleft()}")
