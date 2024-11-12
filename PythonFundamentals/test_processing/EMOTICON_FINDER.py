text = input()
start_indexes = [x for x in range(len(text)) if text[x] == ':']
emoticons = list(text[x: x+2] for x in start_indexes)
print(*emoticons, sep='\n')