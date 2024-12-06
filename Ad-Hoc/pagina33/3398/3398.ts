const fs = require("fs")
const input = fs.readFileSync("/dev/stdin", "utf8").trim().split("\n")
const [moeda, quantia] = input.map(Number)

const result = moeda * quantia

console.log(result.toFixed(2))