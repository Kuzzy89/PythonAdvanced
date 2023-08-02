from collections import deque

food = deque(int(x) for x in input().split(", "))
stamina = deque(int(x) for x in input().split(", "))
day = 1
conquered_peaks = []

peaks = deque([
    ("Vihren", 80),
    ("Kutelo", 90),
    ("Banski Suhodol", 100),
    ("Polezhan", 60),
    ("Kamenitza", 70),
])

while True:
    if len(conquered_peaks) == 5:
        print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
        break

    if day > 7 or not food or not stamina:
        print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")
        break

    a_food = food.pop()
    a_stamina = stamina.popleft()
    energy = a_food + a_stamina
    next_peak = peaks.popleft()

    if energy >= next_peak[1]:
        conquered_peaks.append(next_peak[0])
        day += 1
    else:
        peaks.appendleft(next_peak)
        day += 1

if conquered_peaks:
    print("Conquered peaks:")
    for peak in conquered_peaks:
        print(peak)