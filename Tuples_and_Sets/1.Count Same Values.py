numbers = [float(x) for x in input().split()]
dd = {}

for i in numbers:
    #not the best way
    # if i not in dd:
    #     dd[i] = 1
    # else:
    #     dd[i] += 1
    if i not in dd:
        dd[i] = 0
    dd[i] += 1
for key, value in dd.items():
    print(f"{key} - {value} times")