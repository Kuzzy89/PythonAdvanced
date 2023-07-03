from collections import deque

q = deque()

while True:
    command = input()
    if command == "Paid":
        while q:
            print(q.popleft())
    if command == "End":
        print(f"{len(q)} people remaining.")
        break
    if command == "Paid":
        continue
    q.append(command)
