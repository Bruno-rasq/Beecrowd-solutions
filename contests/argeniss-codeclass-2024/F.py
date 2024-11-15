n = int(input())

for _ in range(n):
    nItems = int(input())
    items = [int(item) for item in input().split()]
    items.sort(reverse=True)

    discount = 0
    while len(items) >= 3:
        discount += items[2]
        items.pop(0)
        items.pop(0)
        items.pop(0)

    print(discount)