clients = {}
rows = int(input())

for x in range(rows):
    token = input().split()
    command = token[0]
    name = token[1]

    if command == 'register':
        name = token[1]
        plate = token[2]
        if name in clients.keys():
            print(f"ERROR: already registered with plate number {clients[name]}")
            continue

        clients[name] = plate
        print(f"{name} registered {plate} successfully")

    elif command == 'unregister':
        if name not in clients.keys():
            print(f"ERROR: user {name} not found")
            continue

        clients.pop(name)
        print(f"{name} unregistered successfully")

clients = dict(sorted(clients.items(), key=lambda item: item[1], reverse=True))
for item in clients.items():
    print(f"{item[0]} => {item[1]}")

