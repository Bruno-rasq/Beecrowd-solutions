def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

n = int(input())
curr = 0
twin = 0

for i in range(n, 0, -1):
    if isPrime(i):
        if curr != 0 and (curr - i) == 2:  # deve ser exatamente 2
            twin = i
            break
        curr = i

print(f"{twin} {curr}")