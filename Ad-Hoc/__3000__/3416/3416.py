alunos, litros, mililitros = [int(n) for n in input().split()]

total_necessario = alunos * mililitros

litros_para_mililitros = litros * 1000

minimo_preparacoes = (total_necessario + litros_para_mililitros - 1) // litros

litros_necessarios = minimo_preparacoes * litros 

print(litros_necessarios)