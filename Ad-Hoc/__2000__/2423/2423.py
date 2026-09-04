class Receita_de_Bolo:
    @staticmethod
    def maximo_bolos(A, B, C):
        #2 xícaras de farinha de trigo (A)
        #3 ovos (B)
        #5 colheres de sopa de leite (C)
        
        bolos_feitos = 0
        while True:
        
            if ((A - 2) < 0) or ((B - 3) < 0) or ((C - 5) < 0): break
        
            bolos_feitos += 1 
            A = A - 2
            B = B - 3
            C = C - 5
            

        print(bolos_feitos)
        
A, B, C = [int(x) for x in input().split()]
Receita_de_Bolo.maximo_bolos(A, B, C)