const fs = require("fs")
const input = fs.readFileSync("/dev/stdin", "utf8").split("").map(Number)

let bits_1 = 0
for (const bit of input){
    bits_1 += bit == 1 ? 1 : 0
}

input.push(bits_1 % 2 == 0 ? 0 : 1)

console.log(input.join(""))