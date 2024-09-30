token = input().split(', ')

if token[len(token) - 1] == 'wolf':
    print('Please go away and stop eating my sheep')
else:
    for i in range(len(token) - 1, -1, -1):
        if token[i] == 'wolf':
            print(f'Oi! Sheep number {len(token) - i - 1}! You are about to be eaten by a wolf!')
            break
