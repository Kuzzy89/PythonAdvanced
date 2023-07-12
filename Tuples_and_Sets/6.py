n = int(input())
even = set()
odd = set()

for x in range(1, n + 1):
    name = input()
    name_sum = 0
    for i in name:
        name_sum += ord(i)

    result = name_sum // x

    if result % 2 == 0:
        even.add(result)
    else:
        odd.add(result)

even_sum = sum(even)
odd_sum = sum(odd)
if even_sum == odd_sum:
    last_res = odd.union(even)
elif even_sum > odd_sum:
    last_res = odd.symmetric_difference(even)
else:
    last_res = odd.difference(even)

print(*last_res, sep=", ")