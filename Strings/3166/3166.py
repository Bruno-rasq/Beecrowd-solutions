class Finding_Words_on_Main_Diagonal:
    above, principal, below = None, None, None

    @staticmethod
    def diagonais_classificadas(grid, n, m):
        diagonals = {}

        for i in range(n):
            for j in range(m):
                key = i - j
                if key not in diagonals:
                    diagonals[key] = []
                diagonals[key].append(grid[i][j])

        Finding_Words_on_Main_Diagonal.principal = "".join(diagonals.get(0, []))
        Finding_Words_on_Main_Diagonal.above = ["".join(diagonals[k]) for k in sorted(diagonals) if k < 0]
        Finding_Words_on_Main_Diagonal.below = ["".join(diagonals[k]) for k in sorted(diagonals) if k > 0]

    @staticmethod
    def find_word(word):
        word = word.lower()
        reversed_word = word[::-1]

        m = Finding_Words_on_Main_Diagonal.principal
        a = Finding_Words_on_Main_Diagonal.above
        b = Finding_Words_on_Main_Diagonal.below

        if word in m or reversed_word in m:
            print(f'1 Palavra "{word}" na diagonal principal')
            return

        for diagonal in a:
            if word in diagonal or reversed_word in diagonal:
                print(f'2 Palavra "{word}" acima da diagonal principal')
                return

        for diagonal in b:
            if word in diagonal or reversed_word in diagonal:
                print(f'3 Palavra "{word}" abaixo da diagonal principal')
                return

        print(f'4 Palavra "{word}" inexistente')


# Entrada
amount_words, N, M = [int(x) for x in input().split()]
words = [input().strip().lower() for _ in range(amount_words)]
puzzle = [[char.lower() for char in input().strip()] for _ in range(N)]

Finding_Words_on_Main_Diagonal.diagonais_classificadas(puzzle, N, M)

for word in words:
    Finding_Words_on_Main_Diagonal.find_word(word)