import math

def compute_HP(source: list[int], level: int) -> int:
    BHP, IV, EV = source
    hp = int(((IV + BHP + (math.sqrt(EV) / 8) + 50) * level) / 50) + 10
    return hp

def compute_attributes(source: list[int], level: int) -> int:
    BS, IV, EV = source
    attb = int(((IV + BS + (math.sqrt(EV) / 8)) * level) / 50) + 5
    return attb
   
class Pokemon:
    @staticmethod
    def solve(idx: int) -> None:
        pokemon, level = input().split()
        HP = [int(x) for x in input().split()]
        AT = [int(x) for x in input().split()]
        DF = [int(x) for x in input().split()]
        SP = [int(x) for x in input().split()]
        
        level = int(level)
        
        print("Caso #" + f"{idx}: {pokemon} nivel {level}")
        print(f"HP: {compute_HP(HP, level)}")
        print(f"AT: {compute_attributes(AT, level)}")
        print(f"DF: {compute_attributes(DF, level)}")
        print(f"SP: {compute_attributes(SP, level)}")
        
n = int(input())
for i in range(1, n + 1):
    Pokemon.solve(i)