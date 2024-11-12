
passwords = input().split(', ')

passwords = [
    x for x in passwords
    if 3 <= len(x) <= 16
       and not x.startswith(' ')
       and not x.endswith(' ')
       and all(map(lambda c: (c.isalnum() or c == '-') or c == '_' and c != ' ', x))
]
print(*passwords, sep='\n')