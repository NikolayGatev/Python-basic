number_roms = int(input())
enough_chairs = True
extra_chairs = 0

for x in range(number_roms):
    token = input().split()

    if len(token[0]) < int(token[1]):
        print(f'{int(token[1]) - len(token[0])} more chairs needed in room {x + 1}')
        enough_chairs = False
        continue
    extra_chairs += len(token[0]) - int(token[1])

if enough_chairs:
    print(f'Game On, {extra_chairs} free chairs left')