class We_Are_Going_To_Close:
    @staticmethod
    def resolve():
        funds, cost = [int(x) for x in input().split()]
        days = (funds // cost)
        
        day, month = 21, 7 #-> 21 sep à 31 oct
        
        if day + days > 30:
            day = (day + days) % 30
            month += 1
            
        else: day += days
        
        if month == 7:
            print(f"A UFSC fecha dia {day} de setembro.")
        else:
            print(f"A UFSC fecha dia {day} de outubro.")

We_Are_Going_To_Close.resolve()