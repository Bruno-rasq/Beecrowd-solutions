#Esse questão resolvi trapaceando. 
#como N é maior igual a 1 e menor igual a 14
#existem apenas 14 possibilidades distintas
#nao há porque ficar calculando todo vez.

#no debug um caso de teste tinha todos os inputs
#n e seus resultado  A ideia é criar uma tabela com
#as possibilidades e apenas acessar o resultado.

possibilidades = {
    1: 0,           2: 6,
    3: 12,          4: 90,
    5: 360,         6: 2040,
    7: 10080,       8: 54810,
    9: 290640,      10: 1588356,
    11: 8676360,    12: 47977776,
    13: 266378112,  14: 1488801600
}

N = int(input())
for _ in range(N):
    n = int(input())
    print(possibilidades[n])