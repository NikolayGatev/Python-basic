import math
from math import ceil

times = [int(x) for x in input().split()]
first_time = 0
second_time = 0
n = math.ceil(float(len(times) / 2))
for x in range(n - 1):
    if times[x] == 0:
        first_time *= 0.8
    else:
        first_time += times[x]

    if times[2 * n - x - 2] == 0:
        second_time *= 0.8
    else:
        second_time += times[2 * n - x - 2]

if first_time > second_time:
    print(f'The winner is left with total time: {first_time:.2f}')
else:
    print(f'The winner is right with total time: {second_time:.2f}')