miners = {}

while True:
    miner = input()
    if miner == 'stop':
        break

    if not miner in miners.keys():
        miners[miner] = 0

    miners[miner] += int(input())

for item in miners.items():
    print(f"{item[0]} -> {item[1]}")