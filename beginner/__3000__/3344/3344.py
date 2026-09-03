def brute(n):

    unitarios = [
        4, 3, 3, 5, 4, 4, , 3, 5, 5, 4, 3,
        6, 6, 8, 8, 7, 7, 9, 8, 8, 6
    ]

    decimais = [6, 6, 5, 5, 5, 7, 6, 6]

    if n == 100:
        return 11

    elif n <= 20:
         return unitarios[n]
    else:
        dec = n / 10
        uni = n % 10
        result = decimais[dec - 2]
        if uni != 0:
            result += unitarios[uni]
        
        return result
    

n = int(input())

for _ in range(1000):
    n = brute(n)

print(n)