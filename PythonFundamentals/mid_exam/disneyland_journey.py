budget = float(input())
months = int(input())
save_money = 0

for x in range(1, months + 1):
    if x % 2 != 0:
        save_money -= save_money * 0.16
    elif x % 4 == 0:
        save_money += save_money * 0.25

    save_money += budget / 4

if save_money >= budget:
    print(f'Bravo! You can go to Disneyland and you will have {(save_money - budget):.2f}lv. for souvenirs.')
else:
    print(f'Sorry. You need {(budget - save_money):.2f}lv. more.')