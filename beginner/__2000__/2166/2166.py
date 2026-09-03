def raiz_10_aproximada(n):
    def fracao_continua(k):
        if k == 0:
            return 0
        return 1 / (2 + fracao_continua(k - 1))

    return 1 + fracao_continua(n)


print(f"{raiz_10_aproximada(int(input())):.10f}") 