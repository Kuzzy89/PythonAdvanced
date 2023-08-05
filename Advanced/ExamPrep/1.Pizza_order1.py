from collections import deque

pizzas = deque(int(x) for x in input().split(", ") if 0 < int(x) < 11)
employees = deque(int(x) for x in input().split(", "))

complete_orders = 0

while pizzas and employees:
    pizza = pizzas.popleft()
    employee = employees.pop()

    complete_orders += min(pizza, employee)

    if pizza > employee:
        pizza -= employee
        pizzas.appendleft(pizza)

if not employees:
    print(f"Not all orders are completed.")
    print(f'Orders left: {", ".join([str(x) for x in pizzas])}')
else:
    print(f"All orders are successfully completed!")
    print(f"Total pizzas made: {complete_orders}")
    print(f'Employees: {", ".join([str(x) for x in employees])}')