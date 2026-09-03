qnt_casos = int(input())

for _ in range(qnt_casos):

    qnt_esferas = int(input())
    min_esferas = 0
    
    for i in range(1, qnt_esferas + 1):
        _divisores = 0
        for j in range(1, i + 1):
            if i % j == 0:
                _divisores += 1
        min_esferas += 1 if _divisores % 2 == 0 else 0
        
    print(min_esferas)