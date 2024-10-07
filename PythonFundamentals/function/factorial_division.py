

def factorial_division(a:int, b:int) -> float:
    def factoriel(n:int) -> int:
        if n == 1:
            return 1
        return n * factoriel(n -1)

    return factoriel(a) / factoriel(b)

first_number = int(input())
second_number = int(input())

print(f'{(factorial_division(first_number, second_number)):.2f}')