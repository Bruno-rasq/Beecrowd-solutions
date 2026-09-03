def match(char):
    if char == "C": return "F"
    if char == "F": return "C"
    if char == "B": return "S"
    if char == "S": return "B"

class Stack:
    def __init__(self):
        self.stack = []
        self._top = 0 
        
    def add(self, char):
        self.stack.append(char)
        self._top += 1 
        
    def remove(self):
        self.stack.pop()
        self._top -= 1
        
    def isEmpty(self): 
        return len(self.stack) == 0
        
    def top(self):
        return self.stack[self._top - 1]
        
class Alien_Ribonucleic_Acid:
    @staticmethod
    def resolve():
        
        while True:
            try:
                stack = Stack()
                RNA = input()
                total = 0
                
                for char in RNA:
                    if not stack.isEmpty():
                        if match(char) == stack.top():
                            total += 1
                            stack.remove()
                            continue
                        
                    stack.add(char)
                            
                print(total)
                
            except EOFError: break 

Alien_Ribonucleic_Acid.resolve()