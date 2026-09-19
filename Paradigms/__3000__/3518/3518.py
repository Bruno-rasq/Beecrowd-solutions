N, K = [int(x) for x in input().split()]
times = [int(x) for x in input().split()]

left = 0
sum = 0
ans = 0

for right in range(left, N):
    sum += times[right]
    while sum > K:
        sum -= times[left]
        left += 1
    ans = max(ans, right - left + 1)

print(ans)