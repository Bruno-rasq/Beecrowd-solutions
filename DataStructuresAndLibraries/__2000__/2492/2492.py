# função inversivem -> 1 origem : 1 destino
# função não inversivel -> 1 origem : N destinos
# não é função -> N origens : 1 ou N destinos

class Ilhas_Isoladas:
    @staticmethod
    def define_tipo_funcao(n_ilhas):
        mapa     = {}        # origem -> destino
        origens  = set()
        destinos = set()
        not_a_func = False
        
        for _ in range(n_ilhas):
            entrada = input().split()   # "X -> Y"
            o, d = entrada[0], entrada[2]
            
            if o in mapa and mapa[o] != d:
                not_a_func = True
            
            mapa[o] = d
            origens.add(o)
            destinos.add(d)
            
        if not_a_func: 
            print("Not a function.")
            return
        
        if len(origens) == len(destinos): print("Invertible.")
        else: print("Not invertible.")
        
while True:
    n = int(input())
    if n == 0: break 

    Ilhas_Isoladas.define_tipo_funcao(n)