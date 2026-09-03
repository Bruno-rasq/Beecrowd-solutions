while True:
    try:
        cidadoes, questoes = [int(x) for x in input().split()]
        
        notas = [int(input()) for _ in range(cidadoes)]
        notas_ordenadas = sorted(notas, reverse=True)
        
        for _ in range(questoes):
            questao = int(input()) - 1
            print(notas_ordenadas[questao])
            
    except EOFError:
        break
