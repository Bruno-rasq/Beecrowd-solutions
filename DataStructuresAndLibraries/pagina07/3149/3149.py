from collections import defaultdict

class Solucao:
    def __init__(self, margem_min, n):
        # relatos -> segundos -> index -> nome
        self.relatos = defaultdict(lambda: defaultdict(list))
        self.margem = [
            86400 - (margem_min * 60),  # início do intervalo antes da meia-noite
            86400 + (margem_min * 60)   # fim do intervalo depois da meia-noite
        ]
        self.verificar_relatos(n)

    def verificar_relatos(self, n):
        for index in range(n):
            horario, nome = input().split()
            horas, minutos = map(int, horario.split(":"))
            segundos = horas * 3600 + minutos * 60
            
            if self.margem[0] <= segundos <= 86400:
                self.relatos[segundos][index].append(nome)

            elif 0 <= segundos <= self.margem[1] - 86400:
                segundos += 86400  # empurra o tempo depois da meia-noite pra frente
                self.relatos[segundos][index].append(nome)

    #-> Bucket sort
    def relatos_verdadeiros(self):
        for tempo in sorted(self.relatos):
            for index in sorted(self.relatos[tempo]):
                for nome in self.relatos[tempo][index]:
                    print(nome)

margem, n = [int(x) for x in input().split()]
sol = Solucao(margem, n)
sol.relatos_verdadeiros()