string = input()
string = string.replace(' ', '')
count_chars = {}

for x in string:
    if not x in count_chars.keys():
        count_chars[x] = 0
    count_chars[x] += 1

for item in count_chars.items():
    print(f"{item[0]} -> {item[1]}")