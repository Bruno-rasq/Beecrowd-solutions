const fs = require("fs")
const [x, y] = fs.readFileSync("/dev/stdin", "utf8").split(" ").map(Number)
const resultado = x >= 0 && x <= 432 && y >= 0 && y <= 468
console.log(resultado ? "dentro" : "fora")