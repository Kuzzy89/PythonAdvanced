n = int(input())
ss = set()

for _ in range(n):
    el = input().split()
    ss.update(el)
[print(i) for i in ss]