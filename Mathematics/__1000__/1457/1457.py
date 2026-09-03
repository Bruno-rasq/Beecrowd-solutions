t = int(input())
for _ in range(t):
    data = input()
    K = data.count('!')
    N = int(data[0:len(data) - K])
    
    ans = N
    mul = 1
    while True:
        _next = ans * (N - (mul * K))
        if _next <= 0: break 
        ans = _next
        mul += 1
        
    print(ans)