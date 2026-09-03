#resultados  de 1 à 50 pré-processados (lookup table)
output = [
    1, 3, 7, 11, 17, 23, 31, 39, 49, 59, 71, 83, 97, 111, 127, 
    143, 161, 179, 199, 219, 241, 263, 287, 311, 337, 363, 391, 
    419, 449, 479, 511, 543, 577, 611, 647, 683, 721, 759, 799, 
    839, 881, 923, 967, 1011, 1057, 1103, 1151, 1199, 1249, 1299
]

num_casos_teste = int(input())
for _ in range(num_casos_teste):
    print(output[int(input()) - 1])