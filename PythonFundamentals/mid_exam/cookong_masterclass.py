from math import ceil

budget = float(input())
students = int(input())
price_flour = float(input())
price_eggs = float(input()) * 10
price_apron = float(input())

cost = (students * price_eggs) + (ceil(students * 1.2) * price_apron) + ((students - (students // 5)) * price_flour)

if cost <= budget:
    print(f'Items purchased for {cost:.2f}$.')
else:
    need = cost - budget
    print(f'{need: .2f}$ more needed.')