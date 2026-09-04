class The_Return_of_The_King:
    @staticmethod
    def resolve():
        line = input()
        idx = len(line) - 1 
        
        total, _sum = 0, 0
        while idx >= 0:
            if line[idx] == "0": 
                idx -= 1 
                _sum += 10 
                
            else: _sum += int(line[idx])
            total += 1 
            idx -= 1
            
        average = _sum / total
            
        print(f"{average:.2f}")
        
The_Return_of_The_King.resolve()