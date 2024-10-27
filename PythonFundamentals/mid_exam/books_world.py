sequence = input().split(' | ')
token = input().split()

while 'Stop!' not in token:
    command = token[0]

    if command == 'Join' and token[1] not in sequence:
        sequence.append(token[1])
    elif command == 'Drop' and token[1] in sequence:
        sequence.remove(token[1])
    elif command == 'Replace' and token[1] in sequence and token[2] not in sequence:
        sequence[sequence.index(token[1])] = token[2]
    elif command == 'Prefer' and 0 <= int(token[1])  and 0 <= int(token[2]) and int(token[1]) < len(sequence) and int(token[2]) < len(sequence):
        sequence[int(token[1])], sequence[int(token[2])] = sequence[int(token[2])], sequence[int(token[1])]

    token = input().split()

print(' '.join(sequence))