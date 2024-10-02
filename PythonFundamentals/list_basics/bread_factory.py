events = input().split('|')
energy = 100
coins = 100

for e in events:
    token = e.split('-')
    number = int(token[1])
    type_ = token[0]

    if type_ == 'rest':
        if energy + number >= 100:
            print(f'You gained {100 - energy} energy.')
            energy = 100
        else:
            print(f'You gained {number} energy.')
            energy += number

        print(f'Current energy: {energy}.')
    elif type_ == 'order':
        if energy >= 30:
            print(f'You earned {number} coins.')
            energy -= 30
            coins += number
        else:
            print(f'You had to rest!')
            energy += 50
    else:
        if coins < number:
            print(f'Closed! Cannot afford {type_}.')
            break

        print(f'You bought {type_}.')
        coins -= number
else:
    print('Day completed!')
    print(f'Coins: {coins}')
    print(f'Energy: {energy}')


