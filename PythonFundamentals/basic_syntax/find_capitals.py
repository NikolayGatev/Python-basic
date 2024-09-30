
token = input()
result = []

for i in range(len(token)):
    if token[i].isupper():
        result.append(i)

print(result)