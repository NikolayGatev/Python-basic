
def perfect_number(numbers :int) -> str:
    if numbers < 6 or numbers % 2 != 0:
        return 'It\'s not so perfect.'

    result = sum([x for x in range(1, int(numbers / 2) + 1) if numbers % x == 0])

    if result == numbers:
        return 'We have a perfect number!'

    return 'It\'s not so perfect.'

enter = int(input())

print(perfect_number(enter))