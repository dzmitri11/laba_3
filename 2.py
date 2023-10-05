total_cost = 0

with open('prices.txt', 'r') as file:
    for line in file:
        parts = line.strip().split()
        if len(parts) >= 3:
            quantity = int(parts[1])
            unit_price = int(parts[2])
            line_cost = quantity * unit_price
            total_cost += line_cost
print(f"Общая стоимость заказа: {total_cost}")
