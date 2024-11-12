text = input()
encode_text = [chr(ord(x) + 3) for x in text]
print(*encode_text, sep='')