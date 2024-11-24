const fs = require("fs")
const input = fs.readFileSync("/dev/stdin", "utf8").trim().split('\n')

function eh_primo(n){
    if(n <= 1) return false
    for(let i = 2; i < Math.sqrt(n); i++){
        if(n % i === 0) return false
    }
    return true
}

function contagem(moedas, salto){
    let index = moedas.length - 1
    let soma = 0
    while(index >= 0){
        soma += moedas[index]
        index -= salto
    }
    return soma
}

while(input.length){
    let n = Number(input.shift())
    let moedas = []

    for(let i = 0; i < n; i++){
        moedas.push(Number(input.shift()))
    }

    let salto = Number(input.shift())
    let resultado = contagem(moedas, salto)

    if(eh_primo(resultado)){
        console.log("You're a coastal aircraft. Robbie, a large silver aircraft.")
    } else {
        console.log("Bad boy! I'll hit you.")
    }
}