class Broken_Keyboard:
    @staticmethod
    def resolve(MAX):
        text = input().strip()
        
        from collections import defaultdict
        
        count = defaultdict(int)
        left = 0
        max_len = 0
        
        for right in range(len(text)):
            # adiciona o caractere atual
            count[text[right]] += 1
        
            # se passar do limite, move left
            while len(count) > MAX:
                count[text[left]] -= 1
                if count[text[left]] == 0:
                    del count[text[left]]
                left += 1
        
            # atualiza o tamanho máximo da janela
            max_len = max(max_len, right - left + 1)
        
        print(max_len)
        
   
while True:
    MAX = int(input())
    if MAX == 0: break
    Broken_Keyboard.resolve(MAX)