coded = input().split(' ')

encoded = []

for word in coded:
    token = [x for x in word]
    number = ''
    for x in token:
        if x.isdigit():
            number += str(x)

    token =  token[len(number):]
    token.insert(0, chr(int(number)))

    token[1], token[-1] = token[-1], token[1]

    encoded.append(''.join(token))

print(' '.join(encoded))

