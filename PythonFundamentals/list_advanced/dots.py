


def is_out_of_range(row_:int, coll_:int, fields:[]) -> bool:
    return 0 > row_ or row_ >= len(fields) or 0 > coll_ or len(fields[0]) <= coll_

def counter_dot(current_row: int, current_coll: int, fields:[]):
    if is_out_of_range(current_row, current_coll, fields) or fields[current_row][current_coll] != '.':
        return 0



    fields[current_row][current_coll] = '*'

    counts = 1


    counts += counter_dot(current_row - 1, current_coll, fields)
    counts += counter_dot(current_row + 1, current_coll, fields)
    counts += counter_dot(current_row, current_coll - 1, fields)
    counts += counter_dot(current_row, current_coll + 1, fields)



    return counts

n = int(input())
fields = []

for x in range(n):
    fields.append( input().split())

max_dots = 0

for row in range(n):
    for coll in range(len(fields[0])):
        if fields[row][coll] == '.':
            max_dots = max(max_dots, counter_dot(row, coll, fields))

print(max_dots)
