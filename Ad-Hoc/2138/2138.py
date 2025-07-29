class Most_Frequent_digit:
    
    @staticmethod
    def resolve():  # N <= 10**1000
        while True:
            try:
                num = input().strip()
                if not num:
                    continue
                
                freq = [0]*10
                _max = 0
                
                for c in num:
                    d = int(c)
                    freq[d] += 1
                    
                    # Atualiza se:
                    # - freq[d] é maior, OU
                    # - freq[d] é igual mas d é maior (desempate)
                    if freq[d] > freq[_max] or (freq[d] == freq[_max] and d > _max):
                        _max = d
                
                print(_max)
            
            except EOFError:
                break

Most_Frequent_digit.resolve()