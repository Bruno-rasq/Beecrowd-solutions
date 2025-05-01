casos_teste = int(input())
for _ in range(casos_teste):
    data1 = input()
    data2 = input()
    output= ""
    
    while len(data1) > 0 or len(data2) > 0:
        output += data1[:2] + data2[:2]
        data1 = data1[2:]
        data2 = data2[2:]
        
    print(output)