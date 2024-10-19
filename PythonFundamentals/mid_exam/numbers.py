sequence = list(map(int, input().split()))

token = input().split()

while 'Finish' not in token:
    command = token[0]

    if command == 'Add':
        sequence.append(int(token[1]))
    elif command == 'Remove' and int(token[1]) in sequence:
        sequence.remove(int(token[1]))
    elif command == 'Replace' and int(token[1]) in sequence:
        sequence[sequence.index(int(token[1]))] = int(token[2])
    elif command == 'Collapse':
        sequence = [x for x in sequence if not x  < int(token[1])]

    token = input().split()

print(' '.join(map(str, sequence)))