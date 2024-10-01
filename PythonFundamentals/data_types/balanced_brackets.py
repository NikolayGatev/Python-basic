n = int(input())
count_open = 0
count_close = 0

for i in range(n):
    token = input()
    if token == '(':
        count_open += 1
    elif token == ')':
        count_close += 1

else:
    if count_open == count_close:
        print('BALANCED')
    else:
        print("UNBALANCED")