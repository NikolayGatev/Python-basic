code = input().split()
string = list(input())
result = []
for x in code:
    n = sum([int(i) for i in x])
    result.append(string[n % len(string)])
    string.pop(n % len(string))

print(''.join(result))