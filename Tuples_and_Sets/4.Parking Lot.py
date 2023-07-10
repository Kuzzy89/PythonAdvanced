n = int(input())
ss = set()
for _ in range(n):
    command, number = input().split(", ")
    if command == "IN":
        ss.add(number)
    elif command == "OUT":
        ss.remove(number)
if not ss:
    print("Parking Lot is Empty")
else:
    [print(x) for x in ss]
