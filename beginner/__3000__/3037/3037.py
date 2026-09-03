partidas = int(input())

def pontuacao():
    pontos = 0
    for _ in range(3):
        x, d = [int(x) for x in input().split()]
        pontos += (x * d)
    return pontos

for _ in range(partidas):
    
    maria = 0
    joao = 0
    
    joao += pontuacao()
    maria += pontuacao()
    
    print("JOAO" if joao > maria else "MARIA")