
password = input()

while True:
    token = input()
    if token == 'Complete':
        break

    command, *data = token.split()
    if command == 'Make':
        type_ = data[0]
        idx = int(data[1])
        if type_ == 'Upper':
            password = password[:idx] + password[idx].upper() + password[idx + 1:]
        elif type_ == 'Lower':
            password = password[:idx] + password[idx].lower() + password[idx + 1:]
    elif command == 'Insert':
        index = int(data[0])
        char = data[1]

        password = password[:index] + char + password[index:] # check idx
    elif command == 'Replace':
        ch = data[0]
        value = int(data[1])
        new_char = chr(ord(ch) + value)
        password = password.replace(ch, new_char)
    elif command == 'Validation':
        valid_pass = True
        if len(password) < 8:
            print('Password must be at least 8 characters long!')
            valid_pass = False
        if not all(x.isalnum() or x == '_' for x in password):
            print('Password must consist only of letters, digits and _!')
            valid_pass = False
        if not any(x for x in password if x.isupper()):
            print('Password must consist at least one uppercase letter!')
            valid_pass = False
        if not any(x for x in password if x.islower()):
            print('Password must consist at least one lowercase letter!')
            valid_pass = False
        if not any(x for x in password if x.isdigit()):
            print('Password must consist at least one digit!')
            valid_pass = False
        continue
    else:
        continue


    print(password)

