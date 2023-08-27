from collections import deque

pumps_count = int(input())
counter = 0
pumps = deque()

for _ in range(pumps_count):
    pumps.append([int(x) for x in input().split()])

for attempt in range(pumps_count):
    trunk = 0
    for petrol, distance in pumps:
        trunk = trunk + petrol - distance
        if trunk < 0:
            counter += 1
            pumps.append(pumps.popleft())
            break
else:
    print(counter)