const fs = require("fs")
const [i1, i2] = fs.readFileSync("/dev/stdin", "utf8").split("\n").map(Number)
const condicao = (i1 >= 14 && i2 >= 14) || (i1 >= 18 || i2 >= 18)

console.log(condicao && i1 >= 6 && i2 >= 6 ? "YES" : "NO")