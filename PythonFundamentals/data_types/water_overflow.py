count = int(input())
capacity = 255

for i in range(count):
    current_pour = int(input())
    if current_pour > capacity:
        print('Insufficient capacity!')
        continue

    capacity -= current_pour

else: print(255 - capacity)




