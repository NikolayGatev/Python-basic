table = []
for i in range(3):
    table.append([int(x) for x in (input().split())])
result = 0

for i in range(3):
    if table[0][i] == table[1][i] == table[2][i] == 2 \
        or table[i][0] == table[i][1] == table[i][2] == 2:
        result = 2
        break
    elif table[0][i] == table[1][i] == table[2][i] == 1 \
        or table[i][0] == table[i][1] == table[i][2] == 1:
        result = 3
        break
if result == 0:
    if table[0][0] == table[1][1] == table[2][2] == 2 \
        or table[2][0] == table[1][1] == table[0][2] == 2:
        result = 2
    elif table[0][0] == table[1][1] == table[2][2] == 1 \
        or table[2][0] == table[1][1] == table[0][2] == 1:
        result = 1

if result == 2:
    print('Second player won')
elif result == 1:
    print('First player won')
else:
    print('Draw!')