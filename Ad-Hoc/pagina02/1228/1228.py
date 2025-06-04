while True:
    try:
        qtn_veiculod = int(input())
        
        grid_largada = [int(x) for x in input().split()]
        grid_chegada = [int(x) for x in input().split()]
        
        indices_chegada = {carro: ind for ind, carro in enumerate(grid_chegada)}
        
        ultrapassagens = 0
        
        for i in range(qtn_veiculod):
            for j in range(i + 1, qtn_veiculod):
                veiculo_i = grid_largada[i]
                veiculo_j = grid_largada[j]
                
                if indices_chegada[veiculo_i] > indices_chegada[veiculo_j]:
                    ultrapassagens += 1
            
        print(ultrapassagens)
        
    except EOFError: break