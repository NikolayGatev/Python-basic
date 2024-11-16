import re

pattern = '\d+'
text = input()
result = []
while text:
    current = re.findall(pattern, text)
    result += current
    text = input()
print(' '.join(result))