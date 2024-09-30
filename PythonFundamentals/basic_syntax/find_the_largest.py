num = list(input())
for i in range(len(num)):
    current = num[i]
    for a in range(i + 1, len(num)):
        if num[a] > num[i]:
            num[a], num[i] = num[i], num[a]


print(''.join(num))