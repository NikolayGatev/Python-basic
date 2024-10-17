first_str = input().split(', ')
second_str = input().split(', ')

print([word for word in first_str if any(word in new_word for new_word in second_str)])