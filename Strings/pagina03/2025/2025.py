def corrigir_palavra(palavra):
    if len(palavra) == 10 and palavra[1:9] == "oulupukk":
        return "Joulupukki"
    elif len(palavra) == 11 and palavra[1:9] == "oulupukk" and palavra[-1] == ".":
        return "Joulupukki."
    return palavra

n = int(input())

for _ in range(n):
    linha = input().split()
    linha_corrigida = [corrigir_palavra(palavra) for palavra in linha]
    print(" ".join(linha_corrigida))