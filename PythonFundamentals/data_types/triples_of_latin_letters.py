number = int(input())

for i in range(97, 97 + number):
    for a in range(97, 97 + number):
        for e in range(97, 97 + number):
           print(chr(i) + chr(a) + chr(e))