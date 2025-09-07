class Praque_Vikings:
    @staticmethod
    def decodify_viking_code(code):
        alfabeto = [chr(i) for i in range(65, 91)]
        decode = ""
        for idx in code:
            char = alfabeto[idx - 1]
            decode += char
            alfabeto.pop(idx - 1)
            alfabeto.insert(0, char)
            
        print(decode)
  
instancia = 1      
while True:
    n = int(input())
    if n == 0: break 

    code = [int(x) for x in input().split()]
    print(f"Instancia {instancia}")
    Praque_Vikings.decodify_viking_code(code)
    print()
    instancia += 1