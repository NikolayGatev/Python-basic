token = input()
digits = [int(x) for x in token if x.isdigit()]
letters = [x for x in token if not x.isdigit()]
result = []

for index, element in enumerate(digits):
    if index % 2 == 0:
        result += letters[: element]
        letters = letters[element :]
    else:
        letters = letters[element :]

print(''.join(result))
