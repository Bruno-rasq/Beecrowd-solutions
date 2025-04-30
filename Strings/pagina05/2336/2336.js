//dado um valor N de base ABC devo converter para base 10
//para isso é necessário pegar o indice de cada caracter na tabela
//ASCII - 65, isso porque A em ASCII é 65 mas na base ABC é 0.

//tendo os valores da de cada caracter deve então converte para base 10
//resultado = (resultado * 26 + valor) % (10^9 + 7)

const input = require("fs").readFileSync("/dev/stdin", "utf8").split("\n")
const mod = (10**9) + 7

input.pop()

for(const abc of input){
    let resultado = 0
    for(let char = 0; char < abc.length; char++){
        const chr = abc[char]
        const codigo = chr.charCodeAt(0) - "A".charCodeAt(0)
        resultado = (resultado * 26 + codigo) % mod
    }
    console.log(resultado)
}