class The_Game:
    @staticmethod
    def maximum_number_of_time(phase: str):
        words = [str(word) for word in phase.split()]
        
        max_time = 0
        time = 0
        curr = ""
        for word in words:
            for char in word:
                curr += char
                time += 1
                
                if time > max_time: max_time = time 
                if curr == "jogo" or curr == "perdeu":
                    time = 0
                    
            curr = ""
            
        print(max_time)
        
n_phases = int(input())
for _ in range(n_phases):
    phase = input().lower().replace(".", "").replace(",", "")
    The_Game.maximum_number_of_time(phase)
