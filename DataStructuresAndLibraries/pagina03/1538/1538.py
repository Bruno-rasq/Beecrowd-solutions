alien = "ABCD"
while True:
    n = int(input())
    if n == 0: break

    temp = n ** 2
    resposta = ""
    
    while temp != 0:
        resposta = alien[temp % 4] + resposta
        temp //= 4
        
    
    print(resposta)