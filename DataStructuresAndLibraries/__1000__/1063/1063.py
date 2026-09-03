from collections import deque

class Solucao:
    @staticmethod
    def resolve():
        while (size := int(input())) != 0:
            
            entrada = deque(input().split())
            saida = deque(input().split())
            pilha = deque()
            log = ""
            
            while saida:
                # Se topo da pilha == próximo da saída, removemos
                if pilha and pilha[-1] == saida[0]:
                    pilha.pop()
                    saida.popleft()
                    log += "R"
                # Senão, se tem mais elementos na entrada, empilhamos
                elif entrada:
                    pilha.append(entrada.popleft())
                    log += "I"
                # Se não tem mais o que empilhar e não dá pra remover
                else:
                    log += " Impossible"
                    break
            
            print(log)

Solucao.resolve()