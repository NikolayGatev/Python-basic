n = int(input())

def is_prime(number):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print(is_prime(n))




