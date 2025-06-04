N, M = [int(x) for x in input().split()]
matrix = [[int(x) for x in input().split()] for _ in range(N)]

def matrixladder(matrix: list[list[int]], M: int) -> bool:
    linha_apenas_zeros = False
    indice_primeiro = -1

    for linha in matrix:
        
        if linha_apenas_zeros:
            for num in linha:
                if num != 0:
                    return False
            continue
        
        zeros = 0
        for i, num in enumerate(linha):
            if num != 0:
                if i <= indice_primeiro:
                    return False
                indice_primeiro = i
                break
            zeros += 1
            
        if zeros == M: linha_apenas_zeros = True

    return True

print("S" if matrixladder(matrix, M) else "N")