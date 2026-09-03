n = int(input())
for _ in range(n):
    wa, ha, wb, hb = [int(x) for x in input().split()]

    ans = "S" if ((wa < wb and ha < hb) or (wa < hb and ha < wb)) else "N"

    print(ans)