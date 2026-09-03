const fs = require('fs')
const input = fs.readFileSync('/dev/stdin', 'utf-8')
const lines = input.split("\n")

let [qn, litros, refil] = lines.shift().split(" ").map(Number)
let lista = lines.shift().split(' ')
let rico = ""
let index = 0

while(litros > refil){
    litros -= refil
    rico = lista[index]
    index = (index + 1) % lista.length
}

rico = lista[index]

console.log(`${rico} ${litros.toFixed(1)}`)