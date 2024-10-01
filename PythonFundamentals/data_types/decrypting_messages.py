key = int(input())
count = int(input())

for i in(range(count)):
    character = ord(input()) + key

    if i < count -1:
        print(chr(character), end='')
    else:
        print(chr(character))