start = int(input())
end = int(input())

for i in range(start, end + 1):
    if i == end:
        print(chr(i))
    else:
        print(chr(i), end = ' ')