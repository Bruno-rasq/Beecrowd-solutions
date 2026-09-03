#para o funcionamento desta questão é preciso implementar um algoritmo guloso
#este algoritmo tenta chegar diretamento ao presente.

#quando se tenta usar busca em largura ou profundidade  excede o tempo limite.

while True:
    rocks, gift = [int(x) for x in input().split()]
    
    if rocks == gift == 0: break

    jump = 2
    pos = 1
    found = False
    count = 0
    limit =  1000
    
    #se a pedra aonde o presente estiver for maior que 34
    #o sapo sempre será capaz de encontrar o presente
    if gift > 34: found = True
        
    else:
        while pos > 0 and pos < rocks + 1 and count < limit:
            distance = (2 * jump - 1)
            
            if pos == gift:
                found = True
                break
            
            elif pos < gift:
                pos = pos + distance if pos + distance < rocks + 1 else pos - distance
            else:
                pos = pos - distance if pos - distance > 0 else pos + distance
                
            jump += 1
            count += 1
                
    print("Let me try!" if found else "Don't make fun of me!")