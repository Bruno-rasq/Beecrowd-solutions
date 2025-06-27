import sys

# Listas para armazenar as variáveis
declaracoes = []  # Variáveis declaradas (máximo 2)
somas = []        # Variáveis de resultado de soma (máximo 1)

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    tokens = line.split()

    if "+" not in line:
        # Declaração de variável: A := 5
        var, _, val = tokens  # Exemplo: A := 5

        if len(declaracoes) == 2:
            declaracoes.pop(0)  # Remove a mais antiga, para ter no máximo 2 variáveis

        declaracoes.append((var, int(val)))  # Adiciona a nova variável

    else:
        # Soma de variáveis: C := A + B
        var_dest, _, var1, _, var2 = tokens  # Exemplo: C := A + B

        # Verifica se as variáveis A e B existem nas declarações ou na lista de somas
        valor1 = None
        valor2 = None
        
        for var, val in declaracoes:
            if var == var1:
                valor1 = val
            if var == var2:
                valor2 = val

        for var, val in somas:
            if var == var1:
                valor1 = val
            if var == var2:
                valor2 = val

        if valor1 is None or valor2 is None:
            print("Compilation Error")
            sys.exit(0)

        # Se as variáveis existem, faz a soma e armazena o resultado
        soma_resultado = valor1 + valor2

        # Se a variável da soma já existir na lista de somas, substitui
        soma_existente = False
        for idx, (var, _) in enumerate(somas):
            if var == var_dest:
                somas[idx] = (var_dest, soma_resultado)
                soma_existente = True
                break

        if not soma_existente:
            # Se não encontrou a soma para substituir, adiciona na lista
            if len(somas) == 1:
                somas.pop(0)  # Remove a soma mais antiga, para ter no máximo 1 variável de soma

            somas.append((var_dest, soma_resultado))

# Se o programa passou sem erros, imprime "OK"
print("OK")