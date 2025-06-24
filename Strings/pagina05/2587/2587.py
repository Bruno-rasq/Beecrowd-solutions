class Jetique:
    @staticmethod
    def resolve():
        # -> O(N)
        n = int(input())
        for _ in range(n):
            print(Jetique.possible_to_resolve())
            
    @staticmethod
    def possible_to_resolve() -> chr:
        
        in_doubty1 = input()
        in_doubty2 = input()
        incomplete_word = input()
        
        # -> O(M) tal, M <= 15
        index_incomplete_chars = []
        for index, char in enumerate(incomplete_word):
            if char == "_": index_incomplete_chars.append(index)
            
        A, B = index_incomplete_chars
        if in_doubty1[A] == in_doubty2[B] or in_doubty1[B] == in_doubty2[A]:
            return "Y"
            
        return "N"
            

Jetique.resolve()