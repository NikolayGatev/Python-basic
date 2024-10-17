from math import ceil

numbers = [int(x) for x in input().split(', ')]
r = ceil(max(numbers) / 10) + 1

for x in range(1, r):
    print(f'Group of {x * 10}\'s: {[e for e in numbers if (x - 1) *10 < e <= x * 10]}')