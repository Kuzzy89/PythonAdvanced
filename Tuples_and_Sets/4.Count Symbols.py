line = input()
ss = {}

for i in line:
    if i in ss:
        ss[i] += 1
    else:
        ss[i] = 1

for key, value in sorted(ss.items()):
    print(f"{key}: {value} time/s")