#mensagem s em bits
bits = [int(x) for x in input()]

bits_1 = 0
for bit in bits:
    if bit == 1:
        bits_1 += 1 
        
if bits_1 % 2 == 0:
    bits.append(0)
else:
    bits.append(1)
    
print("".join(str(n) for n in bits))