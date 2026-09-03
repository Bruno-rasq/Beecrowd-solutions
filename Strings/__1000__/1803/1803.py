
#uma matrix de N colunas por 4 linhas, a primeira e última(F, L)
#colunas são as chaves para decifrar a mensagem, as demais são 
#os caracteres da mensagem.

#formula => CI = (F * Mi + L) % 257 onde MI é a sequência de digitos
#da coluna e Ci o equivalente em ASCII.


matring = [[str(x) for x in input()] for _ in range(4)]

F = int(matring[0][0] + matring[1][0] + matring[2][0] + matring[3][0])
L = int(matring[0][-1] + matring[1][-1] + matring[2][-1] + matring[3][-1])

matring[0] = matring[0][1:-1]
matring[1] = matring[1][1:-1]
matring[2] = matring[2][1:-1]
matring[3] = matring[3][1:-1]

mensagem = ""
for coluna in range(len(matring[0])):  # percorre cada coluna da matring
    MI = matring[0][coluna] + matring[1][coluna] + matring[2][coluna] + matring[3][coluna]
    CI = (F * int(MI) + L) % 257
    mensagem += chr(CI)

print(mensagem)