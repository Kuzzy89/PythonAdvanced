n = int(input())

ss = set()

for _ in range(n):
    ss.add(input())

# for i in ss:
#     print(i)
[print(i) for i in ss]