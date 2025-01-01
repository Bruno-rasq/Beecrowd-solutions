const fs = require("fs")
const input = fs;readFileSync("/dev/stdin", "uft8").split("\n")

const n = Number(input.shift())

for(let i = 1; i < n + 1; i++){
    console.log(`resposta ${i}: ${input.shift()}`)
}