donates = [int(x) for x in (input().split(', '))]
beggars = int(input())

result = []

for i in range(beggars):

    current_beggar = 0
    for e in range(i, len(donates), beggars):
        current_beggar += donates[e]

    result.append(current_beggar)

print(result)