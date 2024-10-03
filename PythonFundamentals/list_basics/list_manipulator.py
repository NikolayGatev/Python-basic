
from sys import maxsize

man_list = [int(x) for x in input().split()]

command = input()

while command != 'end':
    token = command.split()

    if token[0] == 'exchange':
        n = int(token[1]) + 1
        first_list = man_list[:n]
        second_list = man_list[n:]
        man_list = second_list + first_list
    elif token[0] == 'max':
        m = -maxsize
        index = -1
        for n in range(len(man_list)):
            if token[1] == 'odd' and man_list[n] % 2 != 0:
                if man_list[n] > m:
                    m = man_list[n]
                    index = n
            elif token[1] == 'even' and man_list[n] % 2 == 0:
                if man_list[n] > m:
                    m = man_list[n]
                    index = n
        if index > -1:
            print(f'max {token[1]} in on index {index}')
        else:
            print('No matches')
    elif token[0] == 'min':
        m = maxsize
        index = -1
        for n in range(len(man_list)):
            if token[1] == 'odd' and man_list[n] % 2 != 0:
                if man_list[n] < m:
                    m = man_list[n]
                    index = n
            elif token[1] == 'even' and man_list[n] % 2 == 0:
                if man_list[n] < m:
                    m = man_list[n]
                    index = n
        if index > -1:
            print(f'min {token[1]} in on index {index}')
        else:
            print('No matches')
    elif token[0] == 'first':
        number = int(token[1])
        result = []
        counter = 0
        for item in man_list:
            if token[2] == 'odd' and item % 2 != 0:
                result.append(item)
                counter += 1
            elif token[2] == 'even' and item % 2 == 0:
                result.append(item)
                counter += 1
            if counter == number:
                print(result)
                break
        else:
            print(result)
    elif token[0] == 'last':
        number = int(token[1])
        result = []
        counter = 0
        for x in range(len(man_list) -1, -1, -1):
            if token[2] == 'odd' and man_list[x] % 2 != 0:
                result.append(man_list[x])
                counter += 1
            elif token[2] == 'even' and man_list[x] % 2 == 0:
                result.append(man_list[x])
                counter += 1
            if counter == number:
                print(result)
                break
        else:
            print(result)

    command = input()

print(man_list)