data = [int(x) for x in input().split()]

total_hot_dogs_consumidos = data[0]
total_participantes = data[1]

media_hot_dogs_consumidos = total_hot_dogs_consumidos / total_participantes

print(f'{media_hot_dogs_consumidos:.2f}')