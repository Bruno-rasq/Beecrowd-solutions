const fs = require("fs")
const input = fs.readFileSync("/dev/std", "utf8").trim().split('\n')

let carrinhos = 0
let bonecas = 0

for(let i = 0; i < input.length; i++){
    let [nome, sexo] = input[i].split(' ')
    if(sexo == "M"){ carrinhos++ }
    else{ bonecas++ }
}

console.log(`${carrinhos} carrinhos`)
console.log(`${bonecas} bonecas`)