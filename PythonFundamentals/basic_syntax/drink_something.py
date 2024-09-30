age = int(input())
type_drink = ''

if age <= 14:
    type_drink = 'toddy'
elif age <= 18:
    type_drink = 'coke'
elif age <= 21:
    type_drink = 'beer'
else:
    type_drink = 'whisky'

print(f'drink {type_drink}')