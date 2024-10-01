
snowballs = int(input())
high_quality = 0
output = ''

for i in range(snowballs):
    weight = int(input())
    time = int(input())
    quality = int(input())

    value = (weight / time) ** quality
    if value > high_quality:
        high_quality = value
        output = f'{weight} : {time} = {int(high_quality)} ({quality})'

else:
    print(output)




