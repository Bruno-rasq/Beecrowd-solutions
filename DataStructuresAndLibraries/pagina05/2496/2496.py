class Solucao:
    @staticmethod
    def verificar_posicoes_invalidas(size: int, tokens: str) -> int:
        
        indexs = [ord(char) - 65 for char in tokens]
        indexs_sorted = sorted(indexs)
        diferencas = 0
        
        for index, num in enumerate(indexs):
            if num != indexs_sorted[index]:
                diferencas += 1
        
        print("There are the chance." if diferencas <= 2 else "There aren't the chance.")
        
n = int(input())
for _ in range(n):
    Solucao.verificar_posicoes_invalidas(int(input()), input())