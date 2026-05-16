class Decrypt:
    def __init__(self):
        self.row = list(range(26))
        self.col = list(range(26))

    def get_char(self, i):
        if i == 26: return " "
        row_i = self.row[i] # pega a linha real
        col_i = self.col[row_i] # usa a linha para acessar a coluna
        # move a coluna correta (posição row_i)
        self.col.pop(row_i)
        self.col.append(col_i)
        # move a linha (posição i)
        self.row.pop(i)
        self.row.append(row_i)
        return chr(ord('A') + col_i)
   
testCase = 1     
first = True
while True:
    try:
        DEC = Decrypt()
        n = int(input())
        if not first: print()  # linha em branco ANTES do próximo caso
        first = False
        ans = []
        for _ in range(n):
            input_row = [int(x) for x in input().split()]
            input_dec = [DEC.get_char(i - 1) for i in input_row]
            ans.append("".join(input_dec))
        
        print("LISTA #" + f"{testCase}:")
        for out in sorted(ans):
            print(out)
        testCase += 1
            
    except EOFError: break