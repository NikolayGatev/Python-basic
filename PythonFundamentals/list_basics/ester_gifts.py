plan_gifts = input().split()
command = input()
while command != 'No Money':
    token = command.split()

    if token[0] == 'OutOfStock':
        for i in range(len(plan_gifts)):
            plan_gifts[i] = None if plan_gifts[i] == token[1] else plan_gifts[i]
    elif token[0] == 'Required':
        if 0 <= int(token[2]) < len(plan_gifts):
            plan_gifts[int(token[2])] = token[1]
    elif token[0] == 'JustInCase':
        plan_gifts[-1] = token[1]

    command = input()

plan_gifts = filter(None, plan_gifts)
print(*plan_gifts, sep=' ')