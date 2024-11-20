n = int(input())
cars = {}

for _ in range(n):
    car, mileage, fuel = input().split('|')
    cars[car] = {'mileage': int(mileage), 'fuel': int(fuel)}

while True:
    token = input()
    if token == 'Stop':
        break
    command, *data = token.split(' : ')
    if command == "Drive":
        car = data[0]
        distance = int(data[1])
        fuel = int(data[2])
        if cars[car]['fuel'] < fuel:
            print('Not enough fuel to make that ride')
            continue
        cars[car]['fuel'] -= fuel
        cars[car]['mileage'] += distance
        print(f'{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.')
        if cars[car]['mileage'] > 100_000:
            print(f'Time to sell the {car}!')
            cars.pop(car)
    if command == 'Refuel':
        car = data[0]
        fuel = int(data[1])
        current_fuel = cars[car]['fuel']
        cars[car]['fuel'] = min(cars[car]['fuel'] + fuel, 75)
        refuel = cars[car]['fuel'] - current_fuel
        print(f'{car} refueled with {refuel} liters')
    if command == 'Revert':
        car = data[0]
        kilometers = int(data[1])
        cars[car]['mileage'] -= kilometers
        if cars[car]['mileage'] < 10_000:
            cars[car]['mileage'] = 10_000
            continue
        print(f'{car} mileage decreased by {kilometers} kilometers')


for car in cars.items():
    name = car[0]
    mileage = car[1]['mileage']
    fuel = car[1]['fuel']

    print(f'{name} -> Mileage: {mileage} kms, Fuel in the tank: {fuel} lt.')