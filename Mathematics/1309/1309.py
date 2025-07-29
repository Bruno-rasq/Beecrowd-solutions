class Monetary_Formatting:
    @staticmethod
    def resolve():
        while True:
            try:
                num, cents = input(), input()
                partes, curr = [], ""
                
                i = len(num) - 1
                while i >= 0:
                    if len(curr) == 3:
                        partes.append(curr)
                        curr = ""
                
                    curr += num[i]
                    i-=1
                
                partes.append(curr)
                
                money_int = "$" + ",".join([x[::-1] for x in partes][::-1])
                money_cent = "." + cents.rjust(2, "0")
                
                print(money_int + money_cent)
                
            except EOFError: break
        
Monetary_Formatting.resolve()
