from collections import deque

class Building_Designing:
    @staticmethod
    def build(blue_blocks, red_blocks, start_blue):
        count = 0
        curr_size = float('inf')
        is_blue_turn = start_blue
        i, j = 0, 0  # ponteiros para azul e vermelho

        while True:
            if is_blue_turn:
                while i < len(blue_blocks) and blue_blocks[i] >= curr_size:
                    i += 1
                if i >= len(blue_blocks):
                    break
                curr_size = blue_blocks[i]
                count += 1
                i += 1
            else:
                while j < len(red_blocks) and red_blocks[j] >= curr_size:
                    j += 1
                if j >= len(red_blocks):
                    break
                curr_size = red_blocks[j]
                count += 1
                j += 1
            is_blue_turn = not is_blue_turn

        return count

    @staticmethod
    def resolve(blue_blocks, red_blocks):
        # Ordenar decrescente (do maior pro menor)
        blue_blocks.sort(reverse=True)
        red_blocks.sort(reverse=True)

        # Tentar começar com azul ou vermelho
        max_height_blue_first = Building_Designing.build(blue_blocks, red_blocks, start_blue=True)
        max_height_red_first = Building_Designing.build(blue_blocks, red_blocks, start_blue=False)

        print(max(max_height_blue_first, max_height_red_first))


# Leitura da entrada
import sys
input = sys.stdin.read
data = input().split()

index = 0
p = int(data[index])
index += 1

for _ in range(p):
    n = int(data[index])
    index += 1
    blue, red = [], []

    for _ in range(n):
        block = int(data[index])
        index += 1
        if block > 0:
            blue.append(block)
        else:
            red.append(-block)

    Building_Designing.resolve(blue, red)