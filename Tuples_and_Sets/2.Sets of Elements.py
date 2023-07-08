n, m = input().split()
n = int(n)
m = int(m)
n_ss = set()
m_ss = set()

for _ in range(n):
    number = int(input())
    n_ss.add(number)

for _ in range(m):
    number = int(input())
    m_ss.add(number)

d = n_ss.intersection(m_ss)
# for i in d:
#     print(i)
[print(i) for i in d]