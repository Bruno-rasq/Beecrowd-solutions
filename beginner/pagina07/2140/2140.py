def two_bills_is_possible(value):
    bills = [
        150, 120, 110, 105, 102
        70, 60, 55, 52
        30, 25, 22,
        15, 12
        7
    ]

    return True if value in bills else False

while True:
    price, value = [int(n) for n in input().split()]

    if price == 0 and value == 0:
        break

    bills_value = value - price
    response = two_bills_is_possible(bills_value)

    print("possible" if response else "impossible")