from collections import deque


elves_energy = deque([int(x) for x in input().split()])
boxes = [int(x) for x in input().split()]
toys = 0
turns = 0
total_energy_spend = 0

while boxes and elves_energy:
    while elves_energy and elves_energy[0] < 5:
        elves_energy.popleft()

    if not elves_energy:
        break

    elf_energy = elves_energy.popleft()
    box = boxes.pop()

    turns += 1

    toys_to_be_created = 1
    energy_to_be_spend = box
    energy_increase_factor = 1

    if turns % 3 == 0:
        toys_to_be_created = 2
        energy_to_be_spend *= 2
    if turns % 5 == 0:
        toys_to_be_created = 0
        energy_increase_factor = 0

    if energy_to_be_spend <= elf_energy:
        toys += toys_to_be_created
        total_energy_spend += energy_to_be_spend
        elves_energy.append(elf_energy - energy_to_be_spend + energy_increase_factor)
    else:
        boxes.append(box)
        elves_energy.append(elf_energy * 2)

print(f"Toys: {toys}")
print(f"Energy: {total_energy_spend}")
if elves_energy:
    print(f"Elves left: {', '.join([str(x) for x in elves_energy])}")
if boxes:
    print(f"Boxes left: {', '.join([str(x) for x in boxes])}")