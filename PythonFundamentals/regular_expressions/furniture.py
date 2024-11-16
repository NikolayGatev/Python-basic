import re

furniture = []
total_cost = 0
pattern = r'>>([A-Za-z]+)<<(\d+\.?\d*)!(\d+)'
command = input()
while command != 'Purchase':
    match = re.search(pattern, command)
    if match:
        furn, price, quality = match.groups()
        furniture.append(furn)
        total_cost += float(price) * int(quality)

    command = input()

print('Bought furniture:')
for furn in furniture:
    print(furn)
print(f'Total money spend: {total_cost:.2f}')