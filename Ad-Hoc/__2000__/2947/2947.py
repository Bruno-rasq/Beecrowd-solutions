# TODAS AS RESPOSTAS DO DESAFORTUNATO ESTÃO ERRADAS, SABENDO DISSO
# PARA CADA QUESTÃO DEVE CALCULAR A FREQUÊNCIA DE UMA RESPOSTA, O OUTPUT
# É A SOMATÓRIA DA MAIOR FREQUÊNCIA PARA CADA PERGUNTA.

NUM_QUESTIONS = int(input())
DESAFORTUNATO_ANS = input()

# possíveis respostas para cada questão.
answers = [[0 for _ in range(26)] for _ in range(NUM_QUESTIONS)]

NUM_COLLEAGUE = int(input())

for _ in range(NUM_COLLEAGUE):
    gabarit = input()
    for idx in range(NUM_QUESTIONS):
        if DESAFORTUNATO_ANS[idx] != gabarit[idx]:
            ans = ord(gabarit[idx]) - 65
            answers[idx][ans] += 1

MAX_NOTE = 0
for ans in answers:
    MAX_NOTE += max(ans)

print(MAX_NOTE)