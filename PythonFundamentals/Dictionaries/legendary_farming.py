structure = {
    'Shadowmourne': {'shards' : 0}
    ,'Valanyr':{'fragments' : 0}
    ,'Dragonwrath' : {'motes' : 0}
    ,'junk' :{}
}
main = ['shards', 'fragments', 'motes']

not_end = True

while not_end:
    token = input().split()

    for index in range(0, len(token), 2):
        number = int(token[index])
        kind = token[index + 1].lower()

        for item in structure.items():
            if item[0] != 'junk' and kind in item[1].keys():
                item[1][kind] += number
                if item[1][kind] >= 250:
                    not_end = False
                    print(f"{item[0]} obtained!")
                    item[1][kind] -= 250
                    break
            elif item[0] == 'junk' and kind not in main:
                if not kind in item[1].keys():
                    structure[item[0]][kind] = 0
                structure[item[0]][kind] += number

        if not not_end:
            break

for item in structure.items():
    for x in item[1].items():
        print(f"{x[0]}: {x[1]}")
