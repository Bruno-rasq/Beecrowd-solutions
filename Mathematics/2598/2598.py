import math

n = int(input())
for _ in range(n):
    avenue_width, radar_range = [int(x) for x in input().split()]
    amount_radar = math.ceil(avenue_width / radar_range)
    print(amount_radar)