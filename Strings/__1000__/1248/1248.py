class Diet_plain:
    @staticmethod
    def resolve():
        n = int(input())
        for _ in range(n):
            Diet_plain.plain()
            
    @staticmethod
    def plain():
        
        _plain = [str(c) for c in input().strip()]
        breakfast = [str(c) for c in input().strip()]
        lunch = [str(c) for c in input().strip()]
        foods = breakfast + lunch
    
        for char in foods:
            if char in _plain:
                idx = _plain.index(char)
                _plain.pop(idx)
                continue
                
            print("CHEATER")
            return
            
        if len(_plain) == 0: print()
        else: print("".join(sorted(_plain)))

Diet_plain.resolve()