from collections import defaultdict 

class Letter_range:
    @staticmethod
    def resolve():
        while True:
            try:
                entrada = [str(c) for c in input().strip() if c != " "]
                Letter_range.range(sorted(set(entrada)))
            except EOFError: break
    
    @staticmethod # -> sliding window
    def get_intervals(keys: list[str]) -> defaultdict(int):
        
        freq = []
        seq = []
        i = 0
        
        while i < len(keys):
            idx_ascii = ord(keys[i])
            if not seq: seq.append(idx_ascii)
            
            elif idx_ascii == seq[-1] + 1:
                seq.append(idx_ascii)
            else:
                # Fechar intervalo atual
                inicio, fim = chr(seq[0]), chr(seq[-1])
                freq.append(f"{inicio}:{fim}")
                seq = [idx_ascii]  # Começa nova sequência
    
            i += 1
    
        # Após o loop, se sobrar algo em seq, salvar o último intervalo
        if seq:
            inicio, fim = chr(seq[0]), chr(seq[-1])
            freq.append(f"{inicio}:{fim}")
            
        return freq

    @staticmethod
    def range(keys: list[str]) -> None:
        freq = Letter_range.get_intervals(keys)
        if not freq: print()
        else:
            intervals = []
            for interval in sorted(freq):
                intervals.append(interval)
            print(", ".join(intervals))
    
Letter_range.resolve()