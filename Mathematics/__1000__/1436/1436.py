
def quicksort(arr):
    if len(arr) <= 1:
        return arr
        
    pivo = arr[len(arr) // 2]
    left = [x for x in arr if x < pivo]
    middle = [x for x in arr if x == pivo]
    right = [x for x in arr if x > pivo]
    
    return quicksort(left) + middle + quicksort(right)
    
    
cs_teste = int(input())
for i in range(1, cs_teste + 1):
    data = [int(x) for x in input().split()]
    qnt_jogadores = data.pop(0)
    
    idades_ordenadas = quicksort(data)
    
    capitao = idades_ordenadas[qnt_jogadores // 2]
    
    print(f"Case {i}: {capitao}")