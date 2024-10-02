types = input().split('|')
budget = float(input())
profit = 0
sells = []

for x in types:
    token = x.split('->')
    type_ = token[0]
    price = float(token[1])

    if type_ == 'Clothes' and price <= 50 and budget >= price:
        budget -= price
        profit += price * 0.40
        sells.append(price * 1.4)
    elif type_ == 'Shoes' and price <= 35 and budget >= price:
        budget -= price
        profit += price * 0.40
        sells.append(price * 1.4)
    elif type_ == 'Accessories' and price <= 20.5 and budget >= price:
        budget -= price
        profit += price * 0.40
        sells.append(price * 1.4)

sum_ = sum(sells) + budget
formating_sells = ['%.2f' % elem for elem in sells]
print(*formating_sells, sep=' ')
print(f'Profit: {profit:.2f}')
if sum_ < 150:
    print('Not enough money.')
else:
    print('Hello, France!')