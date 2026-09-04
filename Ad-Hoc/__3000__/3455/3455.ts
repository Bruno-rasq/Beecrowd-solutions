const fs = require("fs")
const input = fs.readFileSync("/dev/stdin", "utf8").split("\n")
const [grafica, dinamica, geometrica] = input.shift().split(" ").map(Number)
const questao_desejada = input.shift();

let total = 0;

if(questao_desejada == "A"){
    total += grafica
    total += dinamica * (3/2)
    total += geometrica * 2.5
}
else if (questao_desejada == "B"){
    total += dinamica
    total += grafica * (2/3)
    total += geometrica * 2.5 * (2/3)
}
else if (questao_desejada == "C"){
    total += geometrica
    total += grafica * (1 / 2.5)
    total += dinamica * (3/2) * (1 / 2.5)
}

console.log(Math.floor(total))