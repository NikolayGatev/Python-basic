
def increase_decrease (pokemons_: [], value: int) -> []:
    pokemons_ = [x + value if x <= value else x - value for x in pokemons_]

    return pokemons_

pokemons = list(map(int, input().split()))
removed = 0

while len(pokemons) > 0:
    index = int(input())
    power = 0
    if index < 0:
        power = pokemons[0]
        pokemons[0] = pokemons[-1]
    elif index >= len(pokemons):
        power = pokemons[-1]
        pokemons[-1] = pokemons[0]
    else:
        power = pokemons.pop(index)

    removed += power
    pokemons = increase_decrease(pokemons, power)

print(removed)