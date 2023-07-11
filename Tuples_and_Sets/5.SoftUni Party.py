def is_vip(guest):
    return guest[0].isdigit()


n = int(input())
vip = set()
regular = set()

for _ in range(n):
    reservation = input()
    if is_vip(reservation):
        vip.add(reservation)
    else:
        regular.add(reservation)


while True:
    command = input()
    if command == "END":
        break

    if command in vip:
        vip.remove(command)
    elif command in regular:
        regular.remove(command)

print(len(vip) + len(regular))
[print(x) for x in sorted(vip)]
[print(x) for x in sorted(regular)]