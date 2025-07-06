class SSN_1:
    @staticmethod
    def validate_SSN():
        CPF = input().replace(".", "")
        b1, b2 = 0, 0
        for i in range(9):
            b1 += int(CPF[i]) * (i + 1)
            b2 += int(CPF[i]) * (9 - i)
            
        b1 %= 11
        b2 %= 11
        
        if b1 == 10: b1 = 0
        if b2 == 10: b2 = 0
        
        print("CPF valido" if 
        CPF[-1] == str(b2) and CPF[-2] == str(b1) 
        else "CPF invalido")
    
    @staticmethod
    def resolve():
        while True:
            try: SSN_1.validate_SSN()
            except EOFError: break 
        
SSN_1.resolve()