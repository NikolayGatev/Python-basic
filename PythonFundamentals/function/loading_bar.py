def loading_bar(num :int) -> str:
    if num == 100:
        return '100% Complete!\n[%%%%%%%%%%]'
    num /= 10
    return f'{int(num * 10)}% [{'*'* (int(num))}{'.'*(int(10 - num))}]\nStill loading... '

number = int(input())

print(loading_bar(number))