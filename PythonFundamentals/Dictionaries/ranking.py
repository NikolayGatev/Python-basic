
contests_password = {}
contests_users = {}

while True:
    token = input()
    if token == 'end of contests':
        break
    token = token.split(':')
    contest = token[0]
    password = token[1]
    contests_password[contest] = password

while True:
    token = input()
    if token == 'end of submissions':
        break
    token = token.split('=>')
    contest = token[0]
    password = token[1]
    user = token[2]
    points = int(token[3])

    if contest in contests_password and contests_password[contest] == password:
        if user not in contests_users.keys():
            contests_users[user] = {}
        if contest not in contests_users[user].keys():
            contests_users[user][contest] = 0
        if contests_users[user][contest] < points:
            contests_users[user][contest] = points

users_totals = {user: sum(scores.values()) for user, scores in contests_users.items()}
max_user = max(users_totals, key= users_totals.get)
max_points = users_totals[max_user]
print(f"Best candidate is {max_user} with total {max_points} points.")
print('Ranking')
for item in contests_users.items():
    print(item[0])
    for x in item[1].items():
        print(f"#  {x[0]} -> {x[1]}")
