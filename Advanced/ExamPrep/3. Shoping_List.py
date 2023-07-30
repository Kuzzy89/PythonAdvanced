def shopping_list(budget, **kwargs):
    if budget < 100:
        return "You do not have enough budget."

    reaming_budget = budget

    while reaming_budget:

        bought_items = set()
        bought = []

        for product, product_data in kwargs.items():
            if not product:
                break
            if len(bought_items) == 5:
                break
            price, quantity = product_data[0], product_data[1]
            if price * quantity <= reaming_budget:
                total_price = price * quantity
                reaming_budget -= price * quantity
                bought.append(f"You bought {product} for {total_price:.2f} leva.")
                bought_items.add(product)

        return "\n".join(bought)


print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))

