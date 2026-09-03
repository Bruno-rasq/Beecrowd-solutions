tabela_preprpcessada = {
    "0 0 0 0": "0", "0 0 0 1": "1",
    "0 0 1 0": "1", "0 0 1 1": "X",
    "0 1 0 0": "1", "0 1 0 1": "X",
    "0 1 1 0": "X", "0 1 1 1": "X",
    
    "1 0 0 0": "0", "1 0 0 1": "0",
    "1 0 1 0": "0", "1 0 1 1": "X",
    "1 1 0 0": "0", "1 1 0 1": "X",
    "1 1 1 0": "X", "1 1 1 1": "X"
}

class Elevator:
    @staticmethod
    def resolver():
        n = int(input())
        for _ in range(n):
            print(tabela_preprpcessada[input().strip()])
            
Elevator.resolver()