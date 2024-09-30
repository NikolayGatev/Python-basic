first_string = input()
second_string = input()

old_word = first_string

for i in range(len(first_string)):
    left = second_string[: i + 1]
    right = first_string[i + 1:]

    if old_word != left + right:
        print(left + right)

    old_word = left + right