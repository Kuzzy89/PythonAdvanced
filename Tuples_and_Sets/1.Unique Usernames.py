n = int(input())
ss = set()
for _ in range(n):
    name = input()
    if name not in ss:
        ss.add(name)
        print(name)