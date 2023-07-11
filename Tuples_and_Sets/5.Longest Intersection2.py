n = int(input())
best_intersection = set()

for _ in range(n):
    first, second = input().split("-")
    f_start, f_end = [int(x) for x in first.split(",")]
    sec_start, sec_end = [int(x) for x in second.split(",")]

    first_set = set(range(f_start, f_end + 1))
    second_set = set(range(sec_start, sec_end + 1))
    current_intersection = first_set.intersection(second_set)

    if len(current_intersection) > len(best_intersection):
        best_intersection = current_intersection

print(f"Longest intersection is [{', '.join([str(x) for x in best_intersection])}] with length {len(best_intersection)}")