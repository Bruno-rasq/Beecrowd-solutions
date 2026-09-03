mensagem_dodo = "Os atributos dos monstros vao ser inteligencia, sabedoria..."
mensagem_leo = "Iron Maiden's gonna get you, no matter how far!"
mensagem_pepper = "Urano perdeu algo muito precioso..."
mensagem_empate = "Putz vei, o Leo ta demorando muito pra jogar..."

regras = {
    "pedra":   "tesoura",
    "papel":   "pedra",
    "tesoura": "papel"
}

while True:
    try:
        dodo, leo, pepper = input().split()
        jogadas = [dodo, leo, pepper]
        unicas = set(jogadas)

        if len(unicas) == 1 or len(unicas) == 3:
            print(mensagem_empate)
        else:
            # só duas jogadas diferentes: alguém pode ter ganhado
            for jogada in unicas:
                if jogadas.count(jogada) == 1:
                    if regras[jogada] in jogadas:
                        indice = jogadas.index(jogada)
                        if indice == 0:
                            print(mensagem_dodo)
                        elif indice == 1:
                            print(mensagem_leo)
                        else:
                            print(mensagem_pepper)
                    else:
                        print(mensagem_empate)
    except EOFError:
        break