class Estacionamento:
    def __init__(self, tamanho, qtd_carros):
        self.tam = tamanho
        self.estacionamento = []  # armazena hora de saída
        self.chegadas = []        # armazena hora de entrada
        self.exibir_carros(qtd_carros)
        
    def exibir_carros(self, qtd_carros):
        sucesso = True
        
        for _ in range(qtd_carros):
            hora_entrada, hora_saida = [int(x) for x in input().split()]
            
            # Limpar carros que já saíram
            while self.estacionamento and self.estacionamento[-1] <= hora_entrada:
                self.estacionamento.pop()
                self.chegadas.pop()
            
            # Verificar se está cheia após limpar
            if len(self.estacionamento) >= self.tam:
                sucesso = False
                continue  # não tenta empilhar
            
            # Verificar se pode adicionar
            if not self.estacionamento or hora_saida <= self.estacionamento[-1]:
                # Empilhar
                self.estacionamento.append(hora_saida)
                self.chegadas.append(hora_entrada)
                
                # Verificação extra (igual no código C)
                if len(self.estacionamento) > 1:
                    if not (self.chegadas[-1] > self.chegadas[-2] and
                            self.estacionamento[-1] < self.estacionamento[-2]):
                        sucesso = False
            else:
                sucesso = False  # conflito LIFO
        
        print("Sim" if sucesso else "Nao")

while True:
    qtd_carros, tam_fila = [int(x) for x in input().split()]
    if qtd_carros == tam_fila == 0:
        break
    estacionamento = Estacionamento(tam_fila, qtd_carros)