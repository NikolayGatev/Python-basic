def odd_even_sum(a:str) -> str:
    odd = sum(int(x) for x  in a if int(x) % 2 != 0)
    even = sum(int(x) for x in a if int(x) % 2 == 0)

    return f'Odd sum = {odd}, Even sum = {even}'

first_number = (input())

print(odd_even_sum(first_number))
