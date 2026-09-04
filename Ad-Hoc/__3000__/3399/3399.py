A, B, C, nth = [int(x) for x in input().split()]

diff = abs(B - A)

print(C + (diff * (nth - 3)))