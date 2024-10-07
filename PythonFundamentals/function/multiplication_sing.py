
def multiplication_sing(a:[]) -> str:
    b = 1
    for x in a:
        b *= x

    if b < 0:
        return 'negative'
    elif b > 0:
        return 'positive'
    elif b == 0:
        return 'zero'

x1 = int(input())
x2 = int(input())
x3 = int(input())

print(multiplication_sing([x1, x2, x3]))