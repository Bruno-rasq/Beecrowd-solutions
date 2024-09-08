cases = int(input())

for _ in range(cases):
    a, b [int(ele) for ele in input().split()]

    dicionario = {}

    for _ in range(a):
        key = input()
        value = input()
        dicionario[key] = value

    for _ in range(b):
        palavra = input().split()
        response = ""
        for n in palavra:
            if n not in dicionario:
                response += n
            else:
                response += dicionario[n]
            response += " "
        print(palavra.strip())
        
    print()
    