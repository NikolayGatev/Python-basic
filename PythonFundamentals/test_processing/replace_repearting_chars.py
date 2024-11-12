text = input()
uniques = list(text[0]) + list(text[x] for x in range(1, len(text)) if text[x] != text[x-1])
print(*uniques, sep='')