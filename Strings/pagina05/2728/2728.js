const fs = require("fs")
const input = fs.readFileSync("/dev/stdin", "utf8").split("\n")

const cobol = "cobol"

input.pop() //nao sei porque

for(const line of input){
    const palavras = line.split("-")

    let valido = true

    let ind = 0
    for(const palavra of palavras){
        let letra = cobol[ind]
        let curr = palavra.toLowerCase()

        if(!curr.startsWith(letra) && !curr.endsWith(letra)){
            valido = false;
            break;
        }
        ind++
    }

    console.log(valido ? "GRACE HOPPER": "BUG")
}