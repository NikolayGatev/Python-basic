token = input().split(' | ')
library = {}

for kvp in token:
    key, value = kvp.split(': ')
    if key not in library:
        library[key] = []
    library[key].append(value)

tests = input().split(' | ')
command = input()
if command == "Test":
    for item in library.items():
        if item[0] in tests:
            print(f'{item[0]}:', end='\n -')
            print('\n -'.join(item[1]))
else:
    print(' '.join(library.keys()))