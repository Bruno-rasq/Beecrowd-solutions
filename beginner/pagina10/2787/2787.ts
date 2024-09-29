const fs = require("fs")
const input = fs.readFileSync("/dev/stdin", "utf-8")
const [linha, coluna] = input.split("\n").map(Number)

const isEven = (num: number): boolean => num % 2 == 0

if( (isEven(linha) && isEven(coluna))  || (!isEven(linha) && !isEven(coluna)) ){
    console.log(1)
} else {
    console.log(0)
}