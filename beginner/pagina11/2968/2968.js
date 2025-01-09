const fs = require('fs')
const input = fs.readFileSync("/dev/stdin", "utf8").split(" ").map(Number)
const [voltas, placas] = input

const total_placas = voltas * placas;
let output = []

for(let i = 10; i <= 90; i += 10){
    let qnt_placas_por_porcentagem = Math.ceil((total_placas * i) / 100)
    output.push(qnt_placas_por_porcentagem)
}

console.log(output.join(" ").trim())