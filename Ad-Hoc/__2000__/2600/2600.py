class Tustin_and_His_New_Die:
    @staticmethod
    def resolve():
        numero_casos = int(input())
        
        for _ in range(numero_casos):
            result = Tustin_and_His_New_Die.is_classic_dice()
            print(result)
            
    @staticmethod     
    def is_classic_dice() -> str:
        face2 = int(input())
        face4, face1, face3, face6 = [int(x) for x in input().split()]
        face5 = int(input())
        
        faces = [face1, face2, face3, face4, face5, face6]
        
        # Verifica se tem todos de 1 a 6
        if sorted(faces) != [1, 2, 3, 4, 5, 6]:
            return "NAO"
        
        if (face1 + face6 == 7 and
            face2 + face5 == 7 and
            face3 + face4 == 7):
            return "SIM"
        
        return "NAO"
        
Tustin_and_His_New_Die.resolve()