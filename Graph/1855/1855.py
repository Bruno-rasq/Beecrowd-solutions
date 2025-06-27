class MAP:
    def __init__(self, cols, rows):
        self.cols, self.rows = cols, rows
        self.map = []
        
        for _ in range(rows):
            line = [str(point) for point in input()]
            self.map.append(line)
            
    def in_bounds(self, r, c):
        return 0 <= r < self.rows and 0 <= c < self.cols
        
    def move(self, position, offsety, offsetx, visiteds):
        while True:
            next_r, next_c = position[0] + offsety, position[1] + offsetx
            
            if not self.in_bounds(next_r, next_c) or (next_r, next_c) in visiteds:
                return False  # saiu do mapa ou entrou num loop
            
            next_char = self.map[next_r][next_c]
            
            visiteds.add((next_r, next_c))
            
            position[0], position[1] = next_r, next_c  # atualiza ambas as coordenadas
            
            if next_char == "*": return True  # achou o tesouro!
            if next_char in "><^v": return None  # encontrou nova direção, continue no can_reach_treasure
            if next_char == ".": continue  # segue reto
            
            return False  # caractere inválido
    
    def can_reach_treasure(self):
        visiteds = set()
        position = [0, 0]
        visiteds.add(tuple(position))

        while True:
            heading = self.map[position[0]][position[1]]

            if heading == "*": return True  # achou o tesouro!
            
            if heading == ">": res = self.move(position, 0, 1, visiteds)
            elif heading == "<": res = self.move(position, 0, -1, visiteds)
            elif heading == "^": res = self.move(position, -1, 0, visiteds)
            elif heading == "v": res = self.move(position, 1, 0, visiteds)
            else: return False  # caractere inválido
            
            if res is True: return True       # tesouro
            if res is False: return False      # erro ou loop
            # se res é None, continua o loop e pega nova direção na posição atual
            
class Maesters_Map:
    @staticmethod
    def resolve():
        cols, rows = int(input()), int(input())
        _map = MAP(cols, rows)
        print("*" if _map.can_reach_treasure() else "!")
        
Maesters_Map.resolve()