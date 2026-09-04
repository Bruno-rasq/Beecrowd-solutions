def consistent(numbers):
    numbers.sort()
    for i in range(len(numbers) - 1):
        if numbers[i + 1].startswith(numbers[i]):
            return False
    return True

T = int(input())
for _ in range(T):
    n = int(input())
    numbers = [input().strip() for _ in range(n)]
    print("YES" if consistent(numbers) else "NO")