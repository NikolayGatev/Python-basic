from unicodedata import decimal

count_orders = int(input())
total_value = 0

for i in range(0, count_orders):
    price = float(input())
    days = int(input())
    capsules = int(input())

    if price < 0.01 or price > 100:
        continue

    if days < 1 or days > 31:
        continue

    if capsules < 1 or capsules > 2000:
        continue

    current_price = capsules * days * price
    print(f'The price for the coffee is: ${ current_price:.2f}')
    total_value += current_price

else:
    print(f"Total: ${total_value:.2f}")