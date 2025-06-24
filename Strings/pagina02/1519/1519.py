class Abbreviations:
    @staticmethod
    def resolve():
        while True:
            if (phase := input()) == ".": break
        
            # -> O(26)
            _hash = { chr(i): ["", 0] for i in range(97, 123) }
            
            words = phase.split()
            
            # -> O(N)
            # Primeiro: contar a frequência das palavras
            freq = {}
            for word in words:
                if len(word) >= 3:
                    freq[word] = freq.get(word, 0) + 1
                 
            # -> O(26)   
            # Segundo: escolher a melhor palavra para cada letra
            for word, count in freq.items():
                init_char = word[0]
                gain = count * (len(word) - 2)
                current_gain = _hash[init_char][1]
                
                if gain > current_gain:
                    _hash[init_char] = [word, gain]
            
            # -> O(26)
            # Terceiro: aplicar as abreviações
            chars_nonNull = {key: value for key, value in _hash.items() if value[0] != ""}
            abbrevs = []
            
            # -> O(26)
            word_to_abbrev = { value[0]: f"{key}." for key, value in chars_nonNull.items() }
            
            # -> O(N)
            # Substituir as palavras no texto
            for i in range(len(words)):
                if words[i] in word_to_abbrev:
                    words[i] = word_to_abbrev[words[i]]
            
            # Impressão
            print(" ".join(words))
            print(len(chars_nonNull))
            
            # -> O(K)
            for key in sorted(chars_nonNull):
                word, _ = chars_nonNull[key]
                print(f"{key}. = {word}")
                
Abbreviations.resolve()
