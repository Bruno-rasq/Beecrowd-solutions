const fs = require("fs")
const input = fs.readFileSync("/dev/stdin", "utf8").split(" ")
const [porcentagem1, porcentagem2]: number[] = input.map(Number)

if ( porcentagem2 <= 2 && porcentagem2 >= 0 ) console.log("nova")
else if ( porcentagem2 <= 100 && porcentagem2 >= 97 ) console.log("cheia")
else if ( porcentagem1 < porcentagem2) console.log("crescente")
else console.log("minguante") 