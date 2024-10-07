def return_smallest_number(a:int, b:int) -> str:
    current = ([chr(x) for x in range(a, b)])
    return str.join(' ', current)

first_number = ord(input())
second_number = ord(input())


print(return_smallest_number(first_number + 1, second_number))