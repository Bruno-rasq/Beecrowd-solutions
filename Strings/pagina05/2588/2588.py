class Game_of_Palindromes:
    @staticmethod
    def resolve():
        while True:
            try:
                word = input()
                freq = {}
                for char in word:
                    if char not in freq: freq[char] = 0
                    freq[char] += 1
                    
                amount_odd_chars = 0
                for char in freq:
                    if freq[char] % 2 != 0: amount_odd_chars += 1
                    
                print(amount_odd_chars - 1 if amount_odd_chars != 0 else 0)
            except EOFError: break
                
Game_of_Palindromes.resolve()