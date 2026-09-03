const fs = require("fs")
const input = fs.readFileSync("/dev/stdin", "utf8").split('\n')

let maior = 0
let maior_palavra = ""
let curr = input.shift()

while (curr != '0'){

    let palavras = curr.split(' ')
    let response = []

    for (let i = 0; i < palavras.length; i++){
        if (palavras[i].length >= maior){
            maior = palavra[i].length
            maior_palavra = palavras[i]
        }

        response.push(palavra[i].length)
    }

    console.log(response.join('-'))
    curr = input.shift()
}


console.log('')
console.log(`The biggest word: ${maior_palavra}`)