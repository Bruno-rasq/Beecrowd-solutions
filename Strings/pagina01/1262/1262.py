while True:
    try:
        #cada W incrementa 1 no clock cycles
        #ja os R quando em sequência(maximo procs vezes) contam 1
        
        
        trace = input()
        procs = int(input())
        
        #R -> 1 cycle
        #W -> 1 cycle
        #W -> 1 cycle
        #R -> 1 sewuencia
        #R -> 2 sewuencia
        #R -> 3 sewuencia -> 1 cycle 
        #R -> 1 cycle
        
        #output: 5
        
        clock_cycles = 0
        i = 0
        
        while i < len(trace):
            if trace[i] == "W":
                clock_cycles += 1
                i += 1
            elif trace[i] == "R":
                # Começa um novo ciclo de leitura
                read_count = 0
                while i < len(trace) and trace[i] == "R" and read_count < procs:
                    read_count += 1
                    i += 1
                clock_cycles += 1
                
        print(clock_cycles)
        
    except EOFError: break