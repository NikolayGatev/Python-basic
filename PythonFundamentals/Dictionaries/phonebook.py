phonebook = {}
token = input()
while '-' in token:
    contact = token.split('-')
    phonebook[contact[0]] = contact[1]

    token = input()

for x in range(int(token)):
    name = input()

    if name in phonebook.keys():
        print(f"{name} -> {phonebook[name]}")
    else:
        print(f"Contact {name} does not exist.")
