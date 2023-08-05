from collections import deque

bowls_of_ramen = deque(int(x) for x in input().split(", "))
customers = deque(int(x) for x in input().split(", "))

while customers:
    if not bowls_of_ramen:
        print(f"Out of ramen! You didn't manage to serve all customers.")
        print(f"Customers left: {', '.join(map(str, customers))}")
        #print(f"Customers left: {', '.join([str(x) for x in customers])}")
        break

    bowl = bowls_of_ramen.pop()
    customer = customers.popleft()

    # if bowl == costumer:
    #     bowls_of_ramen.pop(bowl)
    #     customers.popleft(costumer)

    if bowl < customer:
        customers.appendleft(customer - bowl)
    elif bowl > customer:
        bowls_of_ramen.append(bowl - customer)

else:
    print(f"Great job! You served all the customers.")
    if bowls_of_ramen:
        print(f"Bowls of ramen left: {', '.join(map(str, bowls_of_ramen))}")

