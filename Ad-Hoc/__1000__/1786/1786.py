class SSN_2:
    @staticmethod
    def validate_SSN():
        
        CPF = input().replace(".", "")
        
        b1, b2, format_cpf, curr = 0, 0, [], ""
        for i in range(9):
            b1 += int(CPF[i]) * (i + 1)
            b2 += int(CPF[i]) * (9 - i)
            curr += CPF[i]
            if len(curr) == 3: 
                format_cpf.append(curr)
                curr = ""
            
        b1 %= 11
        b2 %= 11
        
        if b1 == 10: b1 = 0
        if b2 == 10: b2 = 0
        
        print(".".join(format_cpf) + f"-{b1}{b2}")
    
    @staticmethod
    def resolve():
        while True:
            try: SSN_2.validate_SSN()
            except EOFError: break 
        
SSN_2.resolve()