#O objetivo desta questão é identificar qual individuo se trata
#usabdo 3 palavras chaves (identificadores) na tabela abaixo

tabela_classificacao = [
    ["vertebrado",   "ave",      "carnivoro",  "aguia"],
    ["vertebrado",   "ave",      "onivoro",    "pomba"],
    ["vertebrado",   "mamifero", "onivoro",    "homem"],
    ["vertebrado",   "mamifero", "herbivoro",  "vaca"],
    
    ["invertebrado", "inseto",   "hematofago", "pulga"],
    ["invertebrado", "inseto",   "herbivoro",  "lagarta"],
    ["invertebrado", "anelideo", "hematofago", "sanguessuga"],
    ["invertebrado", "anelideo", "onivoro",    "minhoca"]
]

chaves_identificacao = [input() for _ in range(3)]

for classificacao in tabela_classificacao:
    A = chaves_identificacao[0]
    B = chaves_identificacao[1]
    C = chaves_identificacao[2]
    
    if A not in classificacao: continue
    if B not in classificacao: continue
    if C not in classificacao: continue

    print(classificacao[3])
    break