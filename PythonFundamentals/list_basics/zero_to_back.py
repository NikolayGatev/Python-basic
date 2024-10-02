give = [int(x) for x in input().split(', ')]
result = []
for x in range(len(give) - 1, -1, -1):
    if give[x] == 0:
        result.append(0)
    else:
        result.insert(0, give[x])
print(result)
