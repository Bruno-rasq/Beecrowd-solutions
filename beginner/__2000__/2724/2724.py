import re

def parse_formula(formula):
    # padrão: letra maiúscula + letra minúscula opcional + dígitos opcionais
    pattern = r'([A-Z][a-z]?)(\d*)'
    result = []
    for element, qty in re.findall(pattern, formula):
        quantity = int(qty) if qty else 1
        result.append(f"{element}{quantity}")
    return result
    
def sliding_window(compostos, comp_perigoso):
    n, m = len(compostos), len(comp_perigoso)
    for i in range(n - m + 1):  # +1 para pegar a última janela
        if compostos[i:i+m] == comp_perigoso:
            return True
    return False

class Help_patatatitu:
    @staticmethod
    def resolve():
        n = int(input())
        for j in range(n):
        
            #possiveis_compostos_perigosos
            PCP = int(input())
            compostos_perigosos = [parse_formula(input()) for _ in range(PCP)]
            
            #compostos do kit 
            CK = int(input())
            for _ in range(CK):
                compostos = parse_formula(input())
                perigoso = False
                for CP in compostos_perigosos:
                    if sliding_window(compostos, CP):
                        perigoso = True
                        break
    
                print("Prossiga" if not perigoso else "Abortar")
                    
            if j < n - 1: print()
            
Help_patatatitu.resolve()