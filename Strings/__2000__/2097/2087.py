class Good_And_Bad_Sets:
    @staticmethod
    def isGoodSet(words, n):
        for i in range(n):
            for j in range(n):
                if i != j and words[i].startswith(words[j]):
                    return False
        return True

while True:
    n = int(input())
    if n == 0: break 

    words = [input() for _ in range(n)]
    isgood = Good_And_Bad_Sets.isGoodSet(words, n)
    out = "Bom" if isgood else "Ruim"
    
    print(f"Conjunto {out}")