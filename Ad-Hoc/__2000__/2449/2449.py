N, K = [int(x) for x in input().split()]
pins = [int(x) for x in input().split()]

ans = 0
aux = 0 
for i in range(N):
    
    diff = K - (pins[i] + aux)
    ans += abs(diff)
    aux = diff


print(ans)