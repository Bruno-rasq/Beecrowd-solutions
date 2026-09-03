n = int(input())
i = 1

fibonacci = [1, 1]
fibonot = []

while len(fibonot) < n:
    
    if i in fibonacci:
        ult = fibonacci[-1]
        pen = fibonacci[-2]
        fibonacci.append(ult + pen)
        
    else:
        fibonot.append(i)
        
    i+= 1
    
print(fibonot[-1])