const fs = require("fs")
const input = Number(fs.readFileSync("/dev/stdin", "utf8"))

const R = Math.sqrt(5)
const fibonacci = ((((1 + R)/2)**input - ((1 - R)/2)**input) / R)

console.log(fibonacci.toFixed(1))