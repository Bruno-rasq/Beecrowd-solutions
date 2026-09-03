def main():
    try:
        num_casos_testes = int(input())
        input()  # Lê a linha em branco após o número de casos
    except EOFError:
        return

    primeiro = True
    for _ in range(num_casos_testes):
        if not primeiro:
            print()

        arvores = {}
        total_arvores = 0

        while True:
            try:
                linha = input()
                if linha == "":
                    break
                if linha not in arvores:
                    arvores[linha] = 0
                arvores[linha] += 1
                total_arvores += 1
            except EOFError:
                # Se acabou o input no meio do último caso
                break

        for arvore in sorted(arvores):
            porcent = (arvores[arvore] * 100) / total_arvores
            print(f"{arvore} {porcent:.4f}")

        primeiro = False

main()
