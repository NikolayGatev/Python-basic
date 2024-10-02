token = [int(x) for x in input().split()]
n = int(input())
order_token = token.copy()
order_token.sort()
for i in range(n):
    token.remove(order_token[i])

print(*token, sep=', ')