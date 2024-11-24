const fs = require("fs")
const input = fs.readFileSync("/dev/stdin", "utf8").trim().split("\n")
const n = Number(input.shift())

for(let i = 0; i < n; i++){
    const [a, b] = input.shift().split(' ').map(Number)
    const pot = BigInt(a) ** BigInt(b)
    const len = pot.toString().length

    console.log(len)
}