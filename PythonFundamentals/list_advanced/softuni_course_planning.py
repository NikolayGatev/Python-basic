
lessons = input().split(', ')
command = input()

while command != 'course start':
    token = command.split(':')

    if token[0] == 'Add' and token[1] not in lessons:
        lessons.append(token[1])
    elif token[0] == 'Insert' and token[1] not in lessons and 0 <= int(token[2]) < len(lessons):
        lessons.insert(int(token[2]), token[1])
    elif token[0] == 'Remove' and token[1] in lessons:
        index = lessons.index(token[1])
        if token[1] in lessons[index + 1]:
            lessons.pop(index + 1)
        lessons.remove(token[1])
    elif token[0] == 'Swap' and token[1] in lessons and token[2] in lessons:
        first_index = lessons.index(token[1])
        second_index = lessons.index(token[2])
        lessons[first_index], lessons[second_index] = lessons[second_index], lessons[first_index]

        if f'{token[1]}-Exercise' in lessons and f'{token[2]}-Exercise' in lessons:
            lessons[first_index + 1], lessons[second_index + 1] = lessons[second_index + 1], lessons[first_index + 1]
        elif f'{token[1]}-Exercise' in lessons:
            lessons.insert(second_index + 1, lessons.pop(first_index + 1))
        elif f'{token[2]}-Exercise' in lessons:
            lessons.insert(first_index + 1, lessons.pop(second_index + 1))
    elif token[0] == 'Exercise':
        if token[1] in lessons and f'{token[1]}-Exercise' not in lessons:
            lessons.insert(lessons.index(token[1]) + 1, f'{token[1]}-Exercise')
        elif token[1] not in lessons:
            lessons.append(token[1])
            lessons.append(f'{token[1]}-Exercise')

    command = input()

for index, x in enumerate(lessons):
    print(f'{index + 1}.{x}')

