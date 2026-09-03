import math

def verificar_interseccao_circulo_retangulo(x0, y0, largura, altura, cx, cy, raio):
    x1, y1 = x0 + largura, y0 + altura

    ponto_mais_proximo_X = max(x0, min(cx, x1))
    ponto_mais_proximo_Y = max(y0, min(cy, y1))

    distancia = math.sqrt(
        (ponto_mais_proximo_X ** 2) + (ponto_mais_proximo_Y ** 2)
    )

    return distancia <= raio

livro_de_magias = {
    "fire":  ["dano": 200, "nivel": [20, 30, 50]],
    "earth": ["dano": 400, "nivel": [25, 55, 70]],
    "water": ["dano": 300, "nivel": [10, 25, 40]],
    "air":   ["dano": 100, "nivel": [18, 38, 60]],
}

casos_teste = int(input())

for _ in range(casos_teste):
    largura, altura, x0, y0 = map(int, input().split())
    magia, nivel, cx, xy = input().split()

    nivel = int(nivel) - 1, cx = int(cx), cy = int(cy)

    raio = livro_de_magias[magia]["nivel"][nivel]
    dano = livro_de_magias[magia]["dano"]

    interseccao = verificar_interseccao_circulo_retangulo(x0, y0, largura, altura, cx, cy, raio)

    print(dano if interseccao else 0)
