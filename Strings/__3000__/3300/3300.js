const fs = require("fs")
const input = fs.readFileSync("/dev/stdin", "utf8").trim()

console.log(
    input.includes('13') ? 
    `${input} es de Mala Suerte` : 
    `${input} NO es de Mala Suerte`
)