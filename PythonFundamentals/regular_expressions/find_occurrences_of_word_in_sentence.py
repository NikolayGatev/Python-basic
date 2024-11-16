import re

text = input()
word = input()
pattern = fr"(?i)\b{word}\b"
print(pattern)

result = re.findall(pattern, text)
print(len(result))