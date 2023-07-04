from collections import deque

init_litters = int(input())
name = input()
q = deque()

while True:
    if name == "Start":
        break
    q.append(name)
    name = input()


new_command = input()
while True:
    if new_command == "End":
        break

    if new_command.startswith("refill "):
        split_command = new_command.split()
        litters = int(split_command[1])
        init_litters += litters

    else:
        person = q.popleft()
        water_wanted = int(new_command)
        if water_wanted <= init_litters:
            print(f"{person} got water")
            init_litters -= water_wanted
        else:
            print(f"{person} must wait")

    new_command = input()

print(f"{init_litters} liters left")