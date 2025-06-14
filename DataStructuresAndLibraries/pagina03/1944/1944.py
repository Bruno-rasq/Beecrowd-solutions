inicial = ["E C A F"]
painel = inicial
brindes = 0

n = int(input())
for _ in range(n):
    text = input()
    if text == painel[0]:
        painel = painel[1:]
        brindes += 1
        if painel == []: painel = inicial
    else: painel = [text[::-1]] + painel
    
print(brindes)