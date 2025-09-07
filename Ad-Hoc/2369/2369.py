class Conta_de_Água:
    @staticmethod
    def convert_m3_in_money(m3):
        money = 0
        for i in range(m3 + 1):
            if i <= 10: money = 7 
            if 11 <= i <= 30: money += 1 
            if 31 <= i <= 100: money += 2 
            if i > 100: money += 5 
            
        print(money)
        
m3 = int(input())
Conta_de_Água.convert_m3_in_money(m3)