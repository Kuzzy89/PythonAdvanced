clothes = [int(x) for x in input().split()]
rack = int(input())
current_capacity = rack
counter = 1

while clothes:
    peace_of_cloth = clothes[-1]
    if current_capacity >= peace_of_cloth:
        clothes.pop()
        current_capacity -= peace_of_cloth
    else:
        current_capacity = rack
        counter += 1
print(counter)