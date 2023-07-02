from collections import deque

quantity = int(input())
orders = deque([int(x) for x in input().split()])
biggest_order = max(orders)
print(biggest_order)

while orders:
    result = quantity - orders[0]

    if result > 0:
        quantity -= orders[0]
        orders.popleft()
    else:
        break

if orders and result < 0:
    orders_to_str = [str(x) for x in orders]
    print(f"Orders left: {' '.join(orders_to_str)}")
else:
    print(f"Orders complete")
