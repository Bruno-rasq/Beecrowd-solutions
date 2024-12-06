def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def fectorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

n = int(input())
numbers = list(map(int, input().split()))

for num in numbers:
    if is_prime(num):
        fact = fectorial(num)
        print(f"{num}! = {fact}")