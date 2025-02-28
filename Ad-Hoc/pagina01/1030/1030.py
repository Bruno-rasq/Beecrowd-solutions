def steps(n , k):
    result = 0
    for i in range(2, n + 1):
        result = (result + k) % i
    return result

n = int(input())
for i in range(n):
    a, b = [int(n) for n in input().split()]
    step = steps(a, b)
    print(f"Case {i + 1}: {step + 1}")