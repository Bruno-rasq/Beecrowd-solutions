const datas = require("fs").readFileSync("/dev/stdin", "utf8");
const inputs = datas.split("\n");

inputs.pop(); // remover linha vazia final

let criancas = {};

for (const crianca of inputs) {
    criancas[crianca.toLowerCase()] = crianca;
}

let lista_ordenada = Object.keys(criancas)
    .sort((a, b) => a.localeCompare(b))
    .map(key => criancas[key]);

console.log(lista_ordenada[lista_ordenada.length - 1]);