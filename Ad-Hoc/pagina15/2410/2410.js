
const fs = require("fs")
const input = fs.readFileSync("/dev/stdin", "utf8").split("\n").map(Number)
const notas = input.shift()

let nota = {}
for(let i = 0; i < notas; i++){
    let curr = input.shift()
    nota[curr] = true
}

console.log(Object.values(nota).length)