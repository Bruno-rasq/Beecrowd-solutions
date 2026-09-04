class Energy_Planning:
    @staticmethod
    def anual_growing_up_rate(year1, consume1, year2, consume2):
        CAGR = (consume2 - consume1) / (year2 - year1)
        # Trunca para 2 casas decimais
        CAGR_truncated = int(CAGR * 100) / 100  
        return f"{CAGR_truncated:.2f}".replace('.', ',')  

teste_cases = int(input())
for _ in range(teste_cases):
    year1, consume1, year2, consume2 = map(int, input().split())
    GWH = Energy_Planning.anual_growing_up_rate(year1, consume1, year2, consume2)
    print(GWH)