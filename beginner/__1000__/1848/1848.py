caws = 0
n = 0

while caws < 3:
    data = input()
    
    if data == "caw caw":
        print(n)
        caws += 1
        n = 0  # reinicia o acumulador para a próxima rodada
    else:
        binario = data.replace("*", "1").replace("-", "0")
        valor = int(binario, 2)
        n += valor