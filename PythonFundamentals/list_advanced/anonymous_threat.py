
names = input().split(' ')
command = input()

while command != '3:1':
    token = command.split()

    if token[0] == 'merge':

        start_index = int(token[1]) if int(token[1]) >= 0 else 0
        end_index = int(token[2]) if int(token[2]) < len(names) else len(names) - 1

        if int(token[1]) >= 0 and int(token[2]) < len(names) and end_index <= start_index:
            continue

        new_merge = ''.join(names[start_index: end_index + 1])
        names= names[:start_index] + [new_merge] + names[end_index + 1:]

    elif token[0] == 'divide':
        index = int(token[1])
        partitions = int(token[2])

        if partitions == 0 or partitions > len(names[index]):
            continue


        word = names[index]

        part_size = len(word) // partitions
        remainder = len(word) % partitions

        new_list = []
        start = 0

        # Create each partition
        for i in range(partitions - 1):
            # Add one more character to the first 'remainder' partitions
            end = start + part_size
            new_list.append(word[start:end])
            start = end
        new_list.append(word[start:])

        names = names[: index] + new_list + names[index + 1:]

    command = input()

print(' '.join(names))
