def data_type(a:str, b:str) -> str:
    if a == 'int':
        return f'{int(b * 2)}'
    if a == 'real':
        return f'{float(b) * 1.5:.2f}'
    if a == 'string':
        return f'${b}%'


first_str = input()
second_str = input()

print(data_type(first_str, second_str))