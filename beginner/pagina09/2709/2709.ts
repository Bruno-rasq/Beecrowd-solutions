const fs = require("fs")
const input = fs.readFileSync("/dev/stdin", "utf8").trim().split('\n')

const eh_primo = (n: number): boolean => {
    if(n <= 1) return false;
    for(let i = 2; i <= Math.sqrt(n); i++){
        if(n % i === 0) return false
    }
    return true
}

const contagem = (moedas: number[], salto: number) : number => {
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
    let moedas: number[] = []

    for(let i = 0; i < n; i++){
        let moeda = Number(input.shift())
        moedas.push(moeda)
    }

    let salto = Number(input.shift())
    let resultado = contagem(moedas, salto)

    console.log(
        eh_primo(resultado) ? 
        "You're a coastal aircraft. Robbie, a large silver aircraft." 
        : "Bad boy! I'll hit you."
    ) 
}