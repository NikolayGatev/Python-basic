phones = list(input().split(', '))

token = input().split(' - ')

while 'End' not in token:
    command = token[0]

    if command == 'Add' and token[1] not in phones:
        phones.append(token[1])
    elif command == 'Remove' and token[1] in phones:
        phones.remove(token[1])
    elif command == 'Bonus phone':
        old, new = token[1].split(':')
        if old in phones:
            phones.insert(phones.index(old) + 1, new)
    elif command == 'Last' and token[1] in phones:
        phones.append(phones.pop(phones.index(token[1])))

    token = input().split(' - ')

print(', '.join(phones))