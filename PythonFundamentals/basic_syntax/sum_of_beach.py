token = input().lower()
letters = ["sand", "water", "fish", "sun"]
count = 0

for letter in letters[:]:
    count += token.count(letter)

print(count)

