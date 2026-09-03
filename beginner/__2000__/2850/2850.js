const fs = require("fs")
const input = fs.readFileSync("/dev/stdin", "utf8").trim().split("\n")

while(input.length){
    let entrada = input.shift()
    if(entrada == "esquerda"){console.log( "ingles") }
    if(entrada == "direita"){ console.log("frances") }
    if(entrada == "nenhuma"){ console.log("portugues") }
    if(entrada == "as duas"){ console.log("caiu") }
}