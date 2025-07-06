class Vigineri_Cipher:
    @staticmethod
    def encrypt(word, key_word, q_start):
        encrypted = ""
        key_len = len(key_word)
        q = q_start  # índice global da chave
        
        for ch in word:
            p = ord(ch) - ord('a')
            k = ord(key_word[q % key_len]) - ord('a')
            c = (p + k) % 26
            encrypted += chr(c + ord('a'))
            q += 1
        
        return encrypted, q  # devolve a palavra criptografada + índice atualizado

class Messaging:
    @staticmethod
    def resolve():
        key_word = input().strip()
        m = int(input())
        
        for _ in range(m):
            message = input().strip().split(" ")
            result = []
            q = 0  # índice global da chave para a linha toda
            
            for word in message:
                if word and word[0] not in "aeiou":
                    encrypted, q = Vigineri_Cipher.encrypt(word, key_word, q)
                    result.append(encrypted)
                else:
                    result.append(word)
            
            print(" ".join(result))
                
Messaging.resolve()