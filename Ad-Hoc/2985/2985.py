class Tobias_Against_the_Clock:
    @staticmethod
    def resolve():
        n = int(input())
        tarefas = []

        for _ in range(n):
            start, duration = map(int, input().split())
            end = start + duration
            tarefas.append((start, end))

        # Ordena pelo horário de término
        tarefas.sort(key=lambda x: x[1])

        count = 0
        fim_atual = -1

        for start, end in tarefas:
            if start >= fim_atual:
                count += 1
                fim_atual = end

        print(count)
            
Tobias_Against_the_Clock.resolve()