class Robert_and_Rampant_Room:
    @staticmethod
    def resolve(n: int) -> None:
        EPR, EHD, INTRUSOS = 0, 0, 0
        
        for _ in range(n):
            matriculo, sigla = input().split()
            
            if sigla == "EPR": EPR += 1
            elif sigla == "EHD": EHD += 1
            else: INTRUSOS += 1
            
        print(f"EPR: {EPR}")
        print(f"EHD: {EHD}")
        print(f"INTRUSOS: {INTRUSOS}")
        
while True:
    try:
        n = int(input())
        Robert_and_Rampant_Room.resolve(n)
    except EOFError: break