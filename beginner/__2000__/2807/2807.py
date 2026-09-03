n = int(input())

fibonacci = [1, 1]

if n > 2:
    while len(fibonacci) < n:
        ult = fibonacci[-1]
        pen = fibonacci[-2]
        fibonacci.append(ult + pen)
        
    iccanobif = sorted(fibonacci, reverse=True)
    print(" ".join([str(n) for n in iccanobif]))
    
elif n == 1:
    print(1)
    
elif n == 2:
    print("1 1")