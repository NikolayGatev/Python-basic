products_quality = {}
products_price = {}

while True:
    token = input().split()
    if 'buy' in token:
        break

    product = token[0]
    price = float(token[1])
    quality = int(token[2])

    if product not in products_quality:
        products_price[product] = 0
        products_quality[product] = 0

    products_quality[product] += quality
    products_price[product] = price

for item in products_quality.items():
    print(f"{item[0]} ->{item[1] * products_price[item[0]]: .2f}")
