import re

count = int(input())
pattern = r'!([A-Z][a-z]{2,})!:\[([A-Za-z]{8,})\]'

for _ in range(count):
    string = input()
    mach = re.match(pattern, string)
    if mach:
        command = mach.group(1)
        code = list(str(ord(x)) for x in mach.group(2))
        print(f'{command}: ', end='')
        print(' '.join(code))
    else:
        print('The message is invalid')