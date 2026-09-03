const fs = require('fs')
const input = fs.readFileSync('/dev/stdin', 'utf-8')
const lines = input.split('\n')

const tem_maiuscula = (str) => /[A-Z]/.test(str)
const tem_minuscula = (str) => /[a-z]/.test(str)
const tem_numero = (str) => /[0-9]/.test(str)

while(lines.length){

    let curr = lines.shift()

    if(curr < 6 || curr > 32){
        console.log(`Senha invalida.`)
        continue
    }

    let maiuscula = false
    let minuscula = false
    let numero = false
    let errado = false
    for(let i = 0; i < curr.length; i++){
        let char = curr[i]
        if(tem_maiuscula(char)){
            maiuscula = true

        } else if (tem_minuscula(char)){
            minuscula = true

        } else if(tem_numero(char)){
            numero = true
        } else {
            errado = true
            break
        }
    }

    if(errado || !(maiuscula && minuscula && numero)){
        console.log(`Senha invalida.`)
    } else {
        console.log(`Senha valida.`)
    }
}