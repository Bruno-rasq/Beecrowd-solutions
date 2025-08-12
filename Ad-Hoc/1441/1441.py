def isEven(hn): return hn % 2 == 0
def EVEN(hn): return (3 * hn) + 1
def ODD(hn): return (0.5 * hn)

memory = {i: 0 for i in range(1, 501)}
memory[1] = 1 

class Hailstone_Sequences:
    @staticmethod
    def max_value(hn):
        
        sequence = []
        sequence.append(hn)
        curr =  EVEN(hn) if isEven(hn - 1) else ODD(hn)
        
        while True:
            sequence.append(int(curr))
            if curr == 1: break
            
            curr = EVEN(curr) if isEven(curr - 1) else ODD(curr)
           
        
        memory[hn] = max(sequence)
        print(memory[hn])
        
while True:
    n = int(input())
    if n == 0: break

    if memory[n] != 0: 
        print(memory[n])
        continue
    
    Hailstone_Sequences.max_value(n)