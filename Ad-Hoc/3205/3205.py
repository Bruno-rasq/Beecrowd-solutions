T = int(input())
for _ in range(T):
    r, e, c = [int(x) for x in input().split()]
    profitAdvertise = e - c
    
    ans = "does not matter"
    
    if profitAdvertise > r:     ans = "advertise"
    elif profitAdvertise < r:   ans = "do not advertise"
    print(ans)