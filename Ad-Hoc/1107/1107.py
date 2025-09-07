# A ideia é somar todas as quedas de altura.
# Primeiro contamos a queda inicial (do topo até a primeira posição).
# Depois, para cada posição, se a altura for menor que a anterior,
# significa que o laser precisou ligar para descer, então somamos essa diferença.

class LaserSculpture:
    @staticmethod
    def count_turns_on(height, length):
        heights = [int(x) for x in input().split()]
        response = height - heights[0]  # queda inicial

        for i in range(1, length):
            if heights[i] < heights[i-1]:
                response += heights[i-1] - heights[i]

        print(response)


while True:
    height, length = [int(x) for x in input().split()]
    if height == length == 0: break
    LaserSculpture.count_turns_on(height, length)