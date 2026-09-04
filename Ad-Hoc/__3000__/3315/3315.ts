
const fs = require("fs")
const input = fs.readFileSync("/dev/stdin", "utf8").split("\n")

function converterParaBinario(n) {
    let binario = "";
    while (n > 0) {
        binario += (n % 2).toString();
        n = Math.floor(n / 2);
    }
    return binario ? binario.split("").reverse().join("") : "0";
}
let mnv = 0;
for(let semana = 0; semana < 4; semana++){
    const visualizacoes = input[i].split(" ").map(Number)
    let soma = 0
    for(let dia = 0; dia < 7; dia++){
        soma += visualizacoes[dia]
    }
    if (soma > mnv) { mnv = soma }
}

console.log(`${mnv} = ${converterParaBinario(mnv)}`)