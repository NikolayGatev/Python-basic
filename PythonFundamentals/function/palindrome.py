def palindrome(numbers :[]) -> []:
    return [str(bool(x == x[::-1])) for x in numbers]

enter = input().split(', ')

print(str.join('\n', palindrome(enter)))