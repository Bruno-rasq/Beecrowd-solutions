class Chocolate_Factory:
    @staticmethod
    def resolve():
        while True:
            a, b, c = [int(x) for x in input().split()]
            if a == b == c == 0: break
        
            volume = a * b * c
            cubo = int(volume ** (1/3))
            
            print(cubo)
            
Chocolate_Factory.resolve()