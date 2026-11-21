n, p, k = [int(x) for x in input().split()]

ans = (p * k) % n

print("SIM" if ans == 0 else "NAO")