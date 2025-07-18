class Frequent_Asked_Questions:
    @staticmethod
    def resolve():
        while True:
            n, k = [int(x) for x in input().split()]
            if n == k == 0: break
        
            frequentes = set()
            freq = {}
            questoes = [int(x) for x in input().split()]
            for questao in questoes:
                if not questao in freq: freq[questao] = 0
                freq[questao] += 1
                if freq[questao] >= k: frequentes.add(questao)
            
            print(len(frequentes))
        
Frequent_Asked_Questions.resolve()