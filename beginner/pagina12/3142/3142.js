const fs = require('fs')
const input = fs.readFileSync("/dev/stdin", 'utf-8')
const lines = input.split('\n')

lines.pop()

function getLetterIndex(letter){
    const alphabetStart = 'A'.charCodeAt(0)
    const letterCode = letter.charCodeAt(0)
    return letterCode - alphabetStart
}

lines.forEach(line => {
    let len = line.length - 1
    let result = 0

    for(let i = 0; i <= len; i++){
        let curr = line[i]
        let column = getLetterIndex(curr)
        result += column  * (26 ** (len - 1))
    }

    console.log(result <= 16384 ? result : "Essa coluna nao existe Tobias!")
})