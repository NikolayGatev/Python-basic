count_strings = int(input())

for i in range(0, count_strings, 1):
    string = input()
    for i in string[::1]:
        if i == ',' or i == '.' or i == '_':
            print(f'{string} is not pure!')
            break
    else:
        print(f'{string} is pure.')