n = int(input())

merged = set()
# 0,3-1,2
# 2,10-3,5
# 6,15-3,10
for _ in range(n):
    first_set = set()
    second_set = set()
    line = input().split("-")
    first = line[0].split(",")
    start_first = int(first[0])
    end_first = int(first[1])
    second = line[1].split(",")
    start_sec = int(second[0])
    end_sec = int(second[1])
    for i in range(start_first, end_first + 1):
        first_set.add(str(i))
    for x in range(start_sec, end_sec + 1):
        second_set.add(str(x))

    current_merged = first_set.intersection(second_set)
    if len(current_merged) > len(merged):
        merged = len(current_merged)

print(f"Longest intersection is [{', '.join([str(x) for x in merged])}] with length {len(merged)}")
