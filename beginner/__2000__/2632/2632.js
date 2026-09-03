const fs = require("fs")
const input = fs.readFileSync("/dev/std", "utf8").trim().split('\n')
const n = Number(input.shift())

const livro_de_magias = {
    "fire":  {"dano": 200, "nivel": [20, 30, 50]},
    "earth": {"dano": 400, "nivel": [25, 55, 70]},
    "water": {"dano": 300, "nivel": [10, 25, 40]},
    "air":   {"dano": 100, "nivel": [18, 38, 60]},
}

for(let i = 0; i < n; i++){

    const [largura, altura, x, y] = input.shift().split(' ').map(Number);
    const [magia, nivel, cx, cy] = input.shift().split(' ')

    const dano = livro_de_magias[magia][dano]
    const nivelIndex = Number(nivel - 1)

    if(nivelIndex < 0 || nivelIndex >= livro_de_magias[magia].nivel.length){
        console.log(0)
        continue
    }

    const raio = livro_de_magias[magia].nivel[nivelIndex]

    let x1 = x + largura, y1 = y + altura;

    const ponto_mais_proximo_x = Math.max(x, Math.min(cx, x1))
    const ponto_mais_proximo_y = Math.max(y, Math.min(cy, y1))

    const distancia = Math.sqrt(
        (ponto_mais_proximo_x ** 2) + (ponto_mais_proximo_y ** 2)
    )

    console.log(distancia <= raio ? dano : 0)
}