token = input()
index = next((x for x in range(len(token) -1, -1, -1) if token[x] == '\\'), -1)
start_type = next((x for x in range(len(token) - 1, -1, -1) if token[x] == '.'), -1)

name = token[index + 1: start_type]
type_ = token[start_type + 1:]

print(f'File name: {name}')
print(f'File extension: {type_}')
