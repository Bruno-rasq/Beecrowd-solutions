const fs = require("fs")
const input = fs.readFileSync("/dev/stdin" , "utf8").split('\n').filter(Boolean)

for(let i = 0; i < input.length; i += 2){

    let bacteria_dn = input[i]
    let code_genetico = input[i + 1]

    console.log(bacteria_dn.includes(code_genetico) ? "Resistente" : "Nao resistente")
}