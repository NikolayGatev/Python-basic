encrypted = input()
decrypted = encrypted

while True:
    token = input()
    if token == 'Decode':
        break

    command, *data = token.split('|')

    if command == 'Move':
        number = int(data[0])
        decrypted = decrypted[number:] + decrypted[:number]
    elif command == 'Insert':
        idx = int(data[0])
        value = data[1]
        decrypted = decrypted[:idx] + value + decrypted[idx:]
    elif command == 'ChangeAll':
        substr = data[0]
        replacement = data[1]
        decrypted = decrypted.replace(substr, replacement)

print(f'The decrypted message is: {decrypted}?')