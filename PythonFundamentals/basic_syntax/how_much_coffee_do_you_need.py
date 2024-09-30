
string = input()
count_coffee = 0

while string != "END":
    if string.lower() == 'coding' or string.lower() == 'cat' or string.lower() == 'dog' or string.lower() == 'movie':
        if string.islower():
            count_coffee += 1
        else:
            count_coffee += 2

    string = input()

if count_coffee > 5:
    print('You need extra sleep')
else:
    print(count_coffee)