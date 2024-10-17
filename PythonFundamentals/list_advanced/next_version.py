from functools import reduce

first_str = input().split('.')
first_str = str(int(reduce(lambda x, y: x + y, first_str)) + 1)

print(*str(first_str), sep='.')
