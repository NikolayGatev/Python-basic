
languages = {}

while True:
    token = input()
    if token == 'exam finished':
        break
    token = token.split('-')
    if token[1] == 'banned' and token[0] in [s for stud in languages.values() for s in stud['students'] ]:
        for l, st in languages.items():
            if token[0] in st['students']:
                st['students'].pop(token[0])
    else:
        name = token[0]
        lang = token[1]
        points = int(token[2])

        if lang not in languages.keys():
            languages[lang] = {'count' : 0, 'students': {}}

        if name not in languages[lang]['students']:
            languages[lang]['students'][name] = points
            languages[lang]['count'] += 1
        else:
            if languages[lang]['students'][name] < points:
                languages[lang]['students'][name] = points
            languages[lang]['count'] += 1


names = {name : sum(lang_data['students'].get(name, 0) for lang_data in languages.values()) for lang_data in languages.values() for name in lang_data['students']}

print('Results:')
for item in names.items():
    print(f"{item[0]} | {item[1]}")

print('Submissions:')
for item in languages.items():
    print(f"{item[0]} - {item[1]['count']}")