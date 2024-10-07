def even_numbers(numbers :[]) -> []:

    return [x for x in numbers if x % 2 == 0]

enter = [int(x) for x in input().split()]

print(even_numbers(enter))