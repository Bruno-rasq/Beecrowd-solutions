NUMERO_UNIVERSIDADES = int(input())
qmt_alunos_por_universidade = [int(x) for x in input().split()]

total_participantes = 0 

for qnt_alunos in qmt_alunos_por_universidade:
    while qnt_alunos % 3 != 0:
        qnt_alunos -= 1
    total_participantes += qnt_alunos
    
print(total_participantes)