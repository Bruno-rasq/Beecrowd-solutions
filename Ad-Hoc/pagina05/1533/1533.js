const fs = require("fs");
const input = fs.readFileSync("/dev/stdin", "utf8").trim().split("\n");

let caso_teste = Number(input.shift());

while (caso_teste !== 0) {
    const suspeitos = input.shift().split(" ").map(Number);

    // Criação de uma cópia do array original para ordenação
    const ordenado = [...suspeitos].sort((a, b) => b - a);

    // O segundo maior valor será o segundo elemento do array ordenado
    const segundo_maior = ordenado[1];

    // Encontrar o índice do segundo maior no array original
    const indice_sg_maior = suspeitos.indexOf(segundo_maior);

    console.log(indice_sg_maior + 1);

    caso_teste = Number(input.shift());
}