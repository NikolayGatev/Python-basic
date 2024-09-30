for row in range(6):
    for col in range(7):
        if ((row == 0 and col % 3 != 0) or
                (row == 1 and col % 3 == 0) or
                (row - col == 2) or
                (row + col == 8)):
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()

num = int(input())
for i in range(1, num +1):
    print('*' * i)


for i in range(9):
    if i == 0 or i == 8:
        print('*' * 5)
    elif i % 2 == 1:
        print()
    else:
        print('*' + 3 * ' ' + '*')

for a in range(2, -1, -1):
    print(' ' * a + (5 - (2 * a)) * '*')
for e in range(1, 3):
    print(' ' * e + (5 - (2 * e)) * '*')
