def matrixsquare(matrix: list[list[int]], N: int) -> None:
    _matrixsquare, justments = [], [0] * N
    
    for line in matrix:
        _newline = []
        for ind, num in enumerate(line):
            
            square = num **2
            _newline.append(square)
            size = len(str(square)) 
            if size > justments[ind]: justments[ind] = size
        
        _matrixsquare.append(_newline)
            
    for i in range(N):
        output = []
        for j in range(N):
            output.append(
                str(_matrixsquare[i][j]).rjust(justments[j])
            )
        print(" ".join(output))
        
    
n, count, first = int(input()), 4, True
for _ in range(n):
    size = int(input())
    matrix = [[int(x) for x in input().split()] for _ in range(size)]
    if not first: print("")
    print(f"Quadrado da matriz #{count}:")
    matrixsquare(matrix, size)
    count += 1
    first = False