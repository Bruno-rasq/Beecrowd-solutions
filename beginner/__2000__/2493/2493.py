def verificar(a, b, resultado, operador):
    if operador == "+":
        return a + b == resultado
    if operador == "-":
        return a - b == resultado
    if operador == "*":
        return a * b == resultado
    if operador == "I":
        # Verifica se nenhuma das operações básicas é válida
        return not (a + b == resultado or a - b == resultado or a * b == resultado)
    return False

while True:
    try:
        t = int(input())
        
        expressoes = []
        acertaram = []
        erraram = []
        
        # Lê as expressões
        for _ in range(t):
            expressoes.append(input())
        
        # Lê as respostas dos jogadores
        for _ in range(t):
            nome, escolhida, resposta = input().split()
            escolhida = int(escolhida)
            
            # Obtém a expressão escolhida
            expressao = expressoes[escolhida - 1]
            partes = expressao.split("=")
            operacao = partes[0].split()
            a = int(operacao[0])
            b = int(operacao[1])
            resultado = int(partes[1])
            
            # Verifica se o jogador acertou ou errou
            if verificar(a, b, resultado, resposta):
                acertaram.append(nome)
            else:
                erraram.append(nome)
        
        # Verifica os resultados e exibe a saída
        if len(acertaram) == t:
            print("You Shall All Pass!")
        elif len(erraram) == t:
            print("None Shall Pass!")
        else:
            erraram.sort()  # Ordena os nomes em ordem alfabética
            print(" ".join(erraram))
    
    except EOFError:
        break