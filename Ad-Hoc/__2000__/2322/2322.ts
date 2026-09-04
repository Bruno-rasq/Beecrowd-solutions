const fs = require("fs")
const input = fs.readFileSync("/dev/stdin", "utf8").split("\n")
const total_pecas = Number(input.shift())
const pecas = input.shift().split(" ").map(Number)

for (let i = 1; i <= total_pecas; i++){
    if(!pecas.includes(i)){
        console.log(i)
        break
    }
}