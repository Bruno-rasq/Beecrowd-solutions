def quicksort(arr: list[tuple[int, int]]):
    if len(arr) <= 1: return arr 
    
    pivo = arr[len(arr) // 2][1]
    left, middle, right = [], [], []
    for ele, num in arr:
        if num < pivo: left.append((ele, num))
        if num == pivo: middle.append((ele, num))
        if num > pivo: right.append((ele, num))
        
    return quicksort(left) + middle + quicksort(right)

while True:
    n_semanas, n_competidores = [int(x) for x in input().split()]

    if n_semanas == n_competidores == 0: break

    competidores = {}
    
    for _ in range(n_semanas):
        rank = [int(x) for x in input().split()]
        for i in range(n_competidores):
            if not rank[i] in competidores:
                competidores[rank[i]] = 0
            competidores[rank[i]] += 1
            
    competidores = quicksort(list(competidores.items()))
    
    del competidores[-1] #-> remove o vencedor
    
    segundo_maior_pontuacao = competidores[-1][1]
    
    competidores_segundo_lugar = [str(id) for id, pontos in competidores if pontos == segundo_maior_pontuacao]
            
    print(" ".join(sorted(competidores_segundo_lugar, key=int)) + " ")
    
    