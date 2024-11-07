contests = {}

while True:
    token = input()
    if token == 'no more time':
        break
    token = token.split(' -> ')
    user = token[0]
    contest = token[1]
    points = int(token[2])

    if contest not in contests.keys():
        contests[contest] = {user : points}
    elif user not in contests[contest].keys():
        contests[contest][user] = points
    else:
        if contests[contest][user] < points:
            contests[contest][user] = points

user_points = {user :sum(user_cont.get(user, 0) for user_cont in contests.values())  for user_cont in contests.values() for user in user_cont.keys()}

for item in contests.items():
    print(f'{item[0]}: {len(item[1])} participants')
    sorted_dict = dict(sorted(item[1].items(), key=lambda item: item[1], reverse=True))
    for index, x in enumerate(sorted_dict.items()):
        print(f"{index + 1}. {x[0]} <::> {x[1]}")

print('Individual standings:')

user_points = dict(sorted(user_points.items(), key=lambda item: item[1], reverse=True ))
for index, item in enumerate(user_points.items()):
    print(f"{index + 1}. {item[0]} -> {item[1]}")