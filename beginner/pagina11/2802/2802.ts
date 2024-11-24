const fs = require("fs")
const input = fs.readFileSync("/dev/stdin", "utf8")
const n = Number(input())

const segmentos = 1 + (((n - 1) * n) / 2) + ((n * (n - 1) * (n - 2) * (n - 3)) / 24);

console.log(segmentos.toFixed(0))
