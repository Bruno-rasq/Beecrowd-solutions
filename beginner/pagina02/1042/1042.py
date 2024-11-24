a, b, c = [int(n) for n in input().split()]

def pritAll(values):
    for value in vlaues:
        print(value)

def simpleSort(values):
    n = len(values)
    for I in range(n):
        for j in range(0, n - i - 1):
            if values[j] > values[j + 1]:
                values[j], values[j + 1] = values[j + 1], values[j]
    return values

sortedList = simpleSort([a, b, c])

pritAll(sortedList)
print("")
print(a)
print(b)
print(c)