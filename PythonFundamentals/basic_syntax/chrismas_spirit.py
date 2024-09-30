
quantity = int(input())
days = int(input())
budget = 0
spirit = 0

ornament_set_price = 2
tree_skirt_price = 5
tree_garland_price = 3
tree_lights_price = 15

ornament_set_points = 5
tree_skirt_points = 3
tree_garland_points = 10
tree_lights_points = 17

for i in range(1, days + 1):
    if i % 11 == 0:
        quantity += 2

    if i % 2 == 0:
        budget += ornament_set_price * quantity
        spirit += ornament_set_points

    if i % 3 == 0:
        budget += tree_skirt_price * quantity
        budget += tree_garland_price * quantity
        spirit += tree_skirt_points
        spirit += tree_garland_points

    if i % 5 == 0:
        budget += tree_lights_price * quantity
        spirit += tree_lights_points

        if i % 3 == 0:
            spirit += 30

    if i % 10 == 0:
        spirit -= 20
        budget += tree_skirt_price
        budget += tree_garland_price
        budget += tree_lights_price
else:
    if days % 10 == 0:
        spirit -= 30

    print(f'Total cost: {budget}')
    print(f'Total spirit: {spirit}')