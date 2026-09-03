s, t, f = list(map(int, input().split()))

time = s + t + f

print((24 + time) % 24)