def sum_numbers(a:int, b:int) -> int:
    return sum([a, b])

def add_and_subtract(a:int, b:int) -> int:
    return a - b

first_number = int(input())
second_number = int(input())
third_number = int(input())

print(add_and_subtract(sum_numbers(first_number, second_number), third_number))