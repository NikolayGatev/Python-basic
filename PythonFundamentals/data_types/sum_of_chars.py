count = int(input())
sum_ = 0

for i in range(count):
    char = input()

    sum_ += ord(char)

print(f'The sum equals: {sum_}')