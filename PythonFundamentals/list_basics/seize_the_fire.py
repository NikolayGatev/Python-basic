
commands = input().split('#')
water = int(input())
effort = 0
cells = []
total = 0

for i in commands:
    token = i.split(' = ')
    if token[0] == 'High' and 81 <= int(token[1]) <= 125 and water >= int(token[1]):
        effort += float(token[1]) * 0.25
        cells.append(token[1])
        water -= int(token[1])
        total += int(token[1])
    elif token[0] == 'Medium' and 51 <= int(token[1]) <= 80 and water >= int(token[1]):
        effort += float(token[1]) * 0.25
        cells.append(token[1])
        water -= int(token[1])
        total += int(token[1])
    elif token[0] == 'Low' and 1 <= int(token[1]) <= 50 and water >= int(token[1]):
        effort += float(token[1]) * 0.25
        cells.append(token[1])
        water -= int(token[1])
        total += int(token[1])

print('Cells:\n - ', end='')
print(*cells, sep='\n - ')
print(f'Effort: {effort:.2f}')
print(f'Total Fire: {total}')