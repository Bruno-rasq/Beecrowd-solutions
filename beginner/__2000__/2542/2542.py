while True:
    try:
        numero_atributos_carta = int(input())
        
        qnt_deck_marcos, qnt_deck_leo = [int(x) for x in input().split()]
        
        deck_marcos = [[int(x) for x in input().split()] for _ in range(qnt_deck_marcos)]
        deck_leo = [[int(x) for x in input().split()] for _ in range(qnt_deck_leo)]
        
        # carta escolhida de marcos e leo
        cm, cl = [int(x) for x in input().split()]
        atributo = int(input())
        
        poder_marcos = deck_marcos[cm - 1][atributo - 1]
        poder_leo = deck_leo[cl - 1][atributo - 1]
        
        if poder_marcos == poder_leo:
            print("Empate")
        else:
            print("Marcos" if poder_marcos > poder_leo else "Leonardo")
    except EOFError:
        break