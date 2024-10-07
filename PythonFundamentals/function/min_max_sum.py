def min_max_sum(numbers :[]) -> str:

    return f'The minimum number is {min(numbers)}\nThe maximum number is {max(numbers)}\nThe sum number is: {sum(numbers)}'

enter = [int(x) for x in input().split()]

print(min_max_sum(enter))