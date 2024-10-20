


def is_ship(row_:int, coll_:int, fields_: list[list[int]]) -> bool:
    return fields_[row_][coll_] != 0

def is_destroyed(health:int) -> bool:
    return health == 1

row = int(input())
fields = []

for x in range(row):
    fields.append(list(map(int, input().split())))

attacks = [[int(e) for e in x.split('-')] for x in input().split()]

destroys = 0

for attack in attacks:
    if is_ship(attack[0], attack[1], fields):
        if is_destroyed(fields[attack[0]][attack[1]]):
            destroys += 1
        fields[attack[0]][attack[1]] -= 1

print(destroys)
