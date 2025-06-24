class Solucao:
    def __init__(self, n_servidore, n_clientes):
        self.servidores = {}
        self.conexoes = 0
        self.set_servidores(n_servidores)
        self.set_conexoes(n_clientes)
        
    def set_servidores(self, n_servidores: int):
        for indice in range(1, n_servidores + 1):
            _, *apps = input().split()
            self.servidores[indice] = apps
            
    def set_conexoes(self, n_clientes):
        for _ in range(n_clientes):
            _, *apps = input().split()
            for servidor in self.servidores:
                for app in apps:
                    if app in self.servidores[servidor]:
                        self.conexoes += 1
                        break
                    
    def get_qnt_conexoes(self): print(self.conexoes)
        
    
while True:
    
    n_servidores, n_clientes = [int(x) for x in input().split()]
    if n_servidores == n_clientes == 0: break

    solucao = Solucao(n_servidores, n_clientes)
    solucao.get_qnt_conexoes()