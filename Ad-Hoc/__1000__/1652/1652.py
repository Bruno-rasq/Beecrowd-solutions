consoantes = ["a", "e", "i", "o", "u"]

def plural_word(word):
    if word[-1] in ["o", "s", "x"]: return word + "es"
    if word[-2:] in ["ch", "sh"]: return word + "es"
    if word.endswith("y") and word[-2] not in consoantes:
        return word[:-1] + "ies"
    
    return word + "s"

from collections import defaultdict
class Deli_Deli:
    irregular_words = defaultdict()
    
    @staticmethod
    def set_irregular_words(n):
        for _ in range(n):
            singular, plural = input().split()
            Deli_Deli.irregular_words[singular] = plural
            
    @staticmethod
    def show_plural_words(n):
        for _ in range(n):
            word = input()
            if word in Deli_Deli.irregular_words: 
                print(Deli_Deli.irregular_words[word])
                continue
                
            print(plural_word(word))
                
                
N, M = [int(x) for x in input().split()]
Deli_Deli.set_irregular_words(N)
Deli_Deli.show_plural_words(M)