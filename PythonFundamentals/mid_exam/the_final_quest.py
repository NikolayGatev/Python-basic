words = input().split()

token = input().split()

while 'Stop' not in token:
    command = token[0]

    if command == 'Delete' and -1 <= int(token[1]) and int(token[1]) < len(words):
        words.pop(int(token[1]) + 1)
    elif 'Swap' == command and token[1] in words and token[2] in words:
        a = words.index(token[1])
        b = words.index(token[2])
        words[a], words[b] = words[b], words[a]
    elif command == 'Put':
        if int(token[2]) == len(words):
            words.append(token[1])
        elif 0 < int(token[2]) and int(token[2]) <= len(words):
            words.insert(int(token[2]) - 1, token[1])
    elif command == 'Sort':
        words.sort(reverse=True)
    elif command == 'Replace' and token[2] in words:
        words[words.index(token[2])] = token[1]

    token = input().split()

print(' '.join(words))