string_one, string_two = input().split()
min_length = min(len(string_one), len(string_two))
result = sum([ord(string_two[x]) * ord(string_one[x]) for x in range(min_length)] + [ord(x) for x in string_two[min_length:]] + [ord(x) for x in string_one[min_length:]] )
print(result)