const fs = require("fs")
const input = fs.readFileSync('/dev/stdin', 'utf-8')
const [ a, b ] = input.split(' ').map(Number)

let loop = 1
while(loop <= b){
    let curr: number[] = []
    for(let i = 0; i < a; i++){
        curr.push(loop)
        loop++
    }
    console.log(curr.join(' '))
    curr = []
}