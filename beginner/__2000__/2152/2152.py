# N logs registrados
n = int(input())

for _ in range(n):
    hora, minuto, log = [int(x) for x in input().split()]
    
    mensagem_a = "A porta abriu!"
    mensagem_b = "A porta fechou!"
    
    horario = f"{hora:02}:{minuto:02}"
    
    LOG = horario + " - "
    LOG += mensagem_a if log == 1 else mensagem_b
    
    print(LOG)