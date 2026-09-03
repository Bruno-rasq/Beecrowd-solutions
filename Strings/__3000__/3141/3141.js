
const fs = require("fs")
const input = fs.readFileSync("/dev/stdin", "utf8").split("\n")
const nome = input[0]
const [ad, am, aa] = input[1].split("/").map(Number)
const [nd, nm, na] = input[2].split("/").map(Number)

if(ad == nd && am == nm) console.log("Feliz aniversario!")

let idade = aa - na
if(am < nm || (am == nm && ad < nd)) idade--

console.log(`Voce tem ${idade} anos ${nome}.`)