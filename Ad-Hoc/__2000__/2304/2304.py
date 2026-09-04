class Banco_imobiliario:
    @staticmethod
    def solve():
        valor_inicial, operacoes = [int(x) for x in input().split()]
        jogadores = {
            "D": valor_inicial, "E": valor_inicial, "F": valor_inicial
        }
        
        for _ in range(operacoes):
            operacao = [str(x) for x in input().split()]
            
            if operacao[0] == "C": #compra
                jogadores[operacao[1]] -= int(operacao[2])
                
            elif operacao[0] == "V": #venda
                jogadores[operacao[1]] += int(operacao[2])
                
            else:
                a, jA, jB, valor = operacao
                jogadores[jA] += int(valor)
                jogadores[jB] -= int(valor)
                
        print(f"{jogadores['D']} {jogadores['E']} {jogadores['F']}")
        
Banco_imobiliario.solve()