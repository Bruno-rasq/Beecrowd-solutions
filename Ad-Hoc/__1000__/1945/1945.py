from collections import defaultdict
class Simulator:
    memory = defaultdict()
    
    @staticmethod
    def set_variables_and_print_last_var():
        last = None
        while True:
            try:
                op = [str(x) for x in input().split()]
                if "+" in op:
                    var, varA, varB = op[0], op[2], op[4]
                    A = Simulator.memory[varA]
                    B = Simulator.memory[varB]
                    Simulator.memory[var] = A + B
                    last = var
                    continue
                
                var, value = op[0], op[2]
                Simulator.memory[var] = int(value)
                last = var
            except EOFError: break
            
        print(Simulator.memory[last])
            
Simulator.set_variables_and_print_last_var()