A, Y, F, P = [int(x) for x in input().split()]

if A % Y == 0:
    print(0)

else:

    days_forward = ((Y - A%Y)% Y) * F
    days_backward = (A % Y) * P

    print(min(days_backward, days_forward))