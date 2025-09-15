#OBS: há uma falha de apresentação na questão que não consegui resolver.

def aligning_the_rings(CS, unlocking_word, criptex):
    for i in range(CS):
        ring = criptex[i]
        unlocking_char = unlocking_word[i]

        # gira até alinhar
        while ring[0] != unlocking_char:
            ring = ring[1:] + ring[0]

        criptex[i] = ring
    return criptex
    
def filter_char_and_ring(secret_word):
    for idx, char in enumerate(secret_word):
        if char != "_":
            return (char, idx)
            
def define_correct_column(criptex, char, ring):
    for idx, ch in enumerate(criptex[ring]):
        if ch == char:
            return idx
        
def decrypt_secret_word(criptex, column):
    msg = ""
    for ring in criptex:
        msg += ring[column]
    return msg

class Da_Vincis_Cryptex:
    @staticmethod
    def decrypt_message(CS, unlocking_word, criptex, secret_word):
        
        aligned_cryptex = aligning_the_rings(CS, unlocking_word, criptex)
        char, ring      = filter_char_and_ring(secret_word)
        column          = define_correct_column(aligned_cryptex, char, ring)
        msg             = decrypt_secret_word(aligned_cryptex, column)
        
        print(unlocking_word + " " + msg)

n_test_cases = int(input())
for case in range(n_test_cases):
    criptex_size, unlocking_word, secret_word = input().split()
    criptex = [input().strip() for _ in range(int(criptex_size))]

    Da_Vincis_Cryptex.decrypt_message(int(criptex_size), unlocking_word, criptex, secret_word)
    
    if case < n_test_cases - 1: input()