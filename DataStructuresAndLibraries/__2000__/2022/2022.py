from collections import defaultdict

class Lista_presentes:
    def __init__(self, nome, tamanho):
        self.nome_crianca = nome,
        self.tamanho_lista = tamanho
        self.presentes = defaultdict(lambda: defaultdict(list))

        for _ in range(self.tamanho_lista):
            nome = input()
            valor, preferencia = input().split()
            self.presentes[int(preferencia)][float(valor)].append(nome)

    def exibir_lista(self):
        print(f"Lista de {self.nome_crianca}")
        for preferencia in sorted(self.presentes, reverse=True):
            for valor in sorted(self.presentes[preferencia]):
                for nome in sorted(self.presentes[preferencia][valor]):
                    print(f"{nome} - R${valor:.02f}")


class Christmas_gifts:
    @staticmethod
    def resolve():
        while True:
            try:
                nome, tamanho_lista = input().split()
                lista = Lista_presentes(nome, int(tamanho_lista))
                lista.exibir_lista()
                print()
            except EOFError: break
            
Christmas_gifts.resolve()
