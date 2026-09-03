const { listenerCount } = require("events");
const fs = require("fs")
const input = fs.readFileSync("/dev/stdin", "utf-8")
const [A, B, C, D] = input.split(" ").map(Number)

const condicao = (B > C && D > A && (C + D) > (A + B) && C >= 0 && D >= 0 && A % 2 == 0)

console.log( condicao ? "Valores aceitos" : "Valores nao aceitos" )
