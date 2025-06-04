def contar_caracteres_semelhantes(original: str, frase: str):
    acertos = []
    contador = 0
    for i in range(len(original)):
        if i < len(frase) and original[i] == frase[i]:
            contador += 1
            acertos.append(i)
    return contador, acertos

n = int(input())
for inst in range(1, n + 1):
    
    original, time1, time2 = input(), input(), input()
    
    r1, acertos1 = contar_caracteres_semelhantes(original, time1)
    r2, acertos2 = contar_caracteres_semelhantes(original, time2)
    
    print(f"Instancia {inst}")
    
    if r1 != r2:
        print("time 1" if r1 > r2 else "time 2")
    else:
        menor_tamanho = min(len(acertos1), len(acertos2))
        vencedor = "empate"
        for j in range(menor_tamanho):
            if acertos1[j] != acertos2[j]:
                vencedor = "time 1" if acertos1[j] < acertos2[j] else "time 2"
                break
        
        if vencedor == "empate":
            if len(acertos1) > len(acertos2):
                vencedor = "time 1"
            elif len(acertos2) > len(acertos1):
                vencedor = "time 2"
        print(vencedor)
    print()