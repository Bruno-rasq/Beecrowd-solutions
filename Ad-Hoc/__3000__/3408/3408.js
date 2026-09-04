const fs = require("fs")
const input = fs.readFileSync("/dev/stdin", "utf8").split("\n")
const n = Number(input.shift())
let soma = 0

const ignore_letters = (line) => {
    const digits = line.split("").filter(char => /^[0-9]$/.test(char)).join("")
    return Number(digits)
}

for(let i = 0; i < n; i++){
    let line = input[i]
    soma += ignore_letters(line)
}

console.log(soma)