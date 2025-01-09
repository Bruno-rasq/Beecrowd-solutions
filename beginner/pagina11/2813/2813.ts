const fs = require("fs")
const input = fs.readFileSync("/dev/stdin", "utf8").split('\n')
const n = Number(input.shift())

let guardachuvaCasa = 0
let guardachuvaTrabalho = 0
let comprasCasa = 0
let comprasTrabalho = 0

for(let i = 0; i < n; i++){
    const [ida, volta] = String(input.shift()).split(' ')

    if(ida == "chuva"){
        guardachuvaCasa > 0 ? guardachuvaCasa-- : comprasCasa++
        guardachuvaTrabalho++
    }

    if(volta == "chuva"){
        guardachuvaTrabalho > 0 ? guardachuvaTrabalho-- : comprasTrabalho++
        guardachuvaCasa++
    }
}

console.log(`${comprasCasa} ${comprasTrabalho}`)