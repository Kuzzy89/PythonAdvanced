ll = [1, 2, 4, 5, 7, 8, 3, -1, 9]
target = 8
targets = set()
values_map = {}

for value in ll:
    if value in targets:
        print(f"{value} + {values_map[value]} = {target}")
    else:
        targets.add(target - value)
        values_map[target - value] = value
