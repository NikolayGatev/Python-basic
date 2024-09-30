
budget = float(input())
flour_price = float(input())
milk_price = flour_price * 1.25 * 0.25
eggs_price = flour_price * 0.75

cost_of_one_bread = flour_price + milk_price + eggs_price
count_bread = 0
color_eggs = 0
while budget > cost_of_one_bread:
    budget -= cost_of_one_bread
    count_bread += 1
    color_eggs += 3

    if count_bread % 3 == 0:
        color_eggs -= (count_bread -2)

print(f'You made {count_bread} loaves of Easter bread! Now you have {color_eggs} eggs and {budget:.2f}BGN left.')