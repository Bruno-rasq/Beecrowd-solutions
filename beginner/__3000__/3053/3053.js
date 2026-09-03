const fs = require('fs')
const input = fs.readFileSync('/dev/stdin', 'utf8')
const lines = input.split('\n')
const trocas = Number(lines.shift())
const moeda = lines.shift().toLowerCase()

let copos = [
    {vazio: moeda === 'a' ? false : true }, //copo A
    {vazio: moeda === 'b' ? false : true }, //copo b
    {vazio: moeda === 'c' ? false : true } //copo C
]

const swap = (pos1, pos2) => {
    let aux = copos[pos1]
    copos[pos1] = copos[pos2]
    copos[pos2] = aux
}

for(let i =0; i < trocas; i++){
    let troca = Number(lines.shift())

    if(troca === 1) swap(0,1)
    if(troca === 2) swap(1,2)
    if(troca === 3) swap(0,2)
}

let index = copos.findIndex(copos => !copos.vazio)

if(index == 1){
    console.log("A")
} else if (index == 2){
    console.log("B")
} else if (index == 3){
    console.log("C")
}