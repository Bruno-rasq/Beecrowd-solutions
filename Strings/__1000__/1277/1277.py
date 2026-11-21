#dado o nome dos alunos e suas frequências registradas
#P para presente, A para ausente e M para justificada
#calcular a frequência de presença do aulo, caso abaixo
#de 75% adicionar o nome na lista de frequencias baixas.
#printar os nomes linha a linha, caso não houver nomes
#printar uma linha em branco.

def calcular_frequencia(total, faltas):
    presencas = total - faltas
    frequencia = (presencas * 100) / total
    return frequencia >= 75

numero_casos = int(input())
for _ in range(numero_casos):
    n = int(input()) #numero de alunos
    
    alunos = [aluno for aluno in input().split()]
    freqnc = [frequ for frequ in input().split()]
    
    alunos_freq_baixa = []
    
    for i in range(n):
        aluno = alunos[i]
        frequencias = freqnc[i]
        
        faltas = 0
        total = 0
        for frequencia in frequencias:
            if frequencia == "A":
                faltas += 1
            if frequencia == "M":
                continue
            total += 1
                
        if not calcular_frequencia(total, faltas):
            alunos_freq_baixa.append(aluno)
        
    print(" ".join(alunos_freq_baixa) if len(alunos_freq_baixa) > 0 else "")