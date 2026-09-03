const fs = require("fs")
const input = fs.readFileSync('/dev/stdin', "utf8").split('\n')

const n = Number(input.shift())

let hobbits = 0
let anoes = 0
let elfos = 0
let humanos = 0
let magos = 0

for(let i = 0; i < n; i++){

    const [nome, raca] = input.shift().split(' ')

    if (raca == "X"){ hobbits += 1}

    if (raca == "H"){ humanos += 1}

    if (raca == "A"){ anoes += 1}

    if (raca == "E"){ elfos  += 1}

    if (raca == "M"){ magos += 1}
}

console.log(`${hobbist} Hobbit(s)`)
console.log(`${humanos} Humano(s)`)
console.log(`${elfos} Elfo(s)`)
console.log(`${anoes} Anao(oes)`)
console.log(`${magos} Mago(s)`)