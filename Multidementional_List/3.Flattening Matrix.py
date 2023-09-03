n = int(input())

result = []

for _ in range(n):
    row = [int(x) for x in input().split(", ")]
    result.append(
        [x for x in row]
    )

flatted = [x for x in result for x in x]
print(flatted)