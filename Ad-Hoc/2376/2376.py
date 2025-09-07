class Copa_do_mundo:
    @staticmethod
    def set_chaves(n_partidas: int, fase_atual):
        proxima_fase = []
        t1, t2 = 0, 1 
        for i in range(n_partidas):
            timeA, timeB = [int(x) for x in input().split()]
            if timeA > timeB: proxima_fase.append(fase_atual[t1])
            if timeA < timeB: proxima_fase.append(fase_atual[t2])
            t1 += 2; t2 += 2
        return proxima_fase
        
    @staticmethod
    def defina_vencedor_copa():
        oitavas = [chr(i) for i in range(65, 80 + 1)]
        quartas = Copa_do_mundo.set_chaves(8, oitavas)
        semifinal = Copa_do_mundo.set_chaves(4, quartas)
        final = Copa_do_mundo.set_chaves(2, semifinal)
        vencedor = None 
        #final    
        timeA, timeB = [int(x) for x in input().split()]
        if timeA > timeB: vencedor = final[0]
        if timeA < timeB: vencedor = final[1]
        
        print(vencedor)
        
Copa_do_mundo.defina_vencedor_copa()