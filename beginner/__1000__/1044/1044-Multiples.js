const fs = require("fs")
const input = fs.readFileSync("/dev/stdin", "utf8").split(" ")
const lines = input.map(el => Number(el))
let [ a, b ] = lines

if(a < b){
    [a ,b] = [b ,a]
}

let resp = a % b === 0 ? 'Sao Multiplos' : 'Nao sao Multiplos';

console.log(resp)