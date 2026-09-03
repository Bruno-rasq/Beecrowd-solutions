Test_cases = int(input())

for _ in range(Test_cases):
    money, n_ingredients, m_cakes = [int(x) for x in input().split()]
    ingredients = [int(x) for x in input().split()]
    ans = 0

    for _ in range(m_cakes):
        qi, *cake_ingredients = [int(x) for x in input().split()]
        cake_price = 0
        i = 0
        j = 1
        for _ in range(qi):
            idx, qnt = cake_ingredients[i], cake_ingredients[j]
            i += 2
            j += 2
            cake_price += ingredients[idx] * qnt

        ans = max(ans, money // cake_price)
        

    print(ans)