sides = {}

while True:
    token = input()
    if token == 'Lumpawaroo':
        break

    if ' | ' in token:
        token = token.split(' | ')
        side = token[0]
        user = token[1]
        if side not in sides.keys() and user not in sides.values():
            sides[side] = [user,]
        elif user not in [u for users in sides.values() for u in users]:
            sides[side].append(user)

    elif ' -> ' in token:
        token = token.split(' -> ')
        side = token[1]
        user = token[0]

        if user in [u for users in sides.values() for u in users]:
            key = next((key for key, value_list in sides.items() if user in value_list), None)
            sides[key].remove(user)
            if side not in sides.keys():
                sides[side] = []
            sides[side].append(user)
        elif side in sides.keys():
            sides[side].append(user)
        else:
            sides[side] = [user,]

        print(f"{user} joins the {side} side!")

for item in sides.items():
    if item[1]:
        print(f"Side: {item[0]}, Members: {len(item[1])}")
    for x in item[1]:
        print(f"! {x}")
