const fs = require('fs')
const input = fs.readFileSync('/dev/stdin', 'utf-8').trim().split('\n')
const N = Number(input.shift())
const nums = input.shift().split(' ').map(Number)

let multi2 = 0
let multi3 = 0
let multi4 = 0
let multi5 = 0

for(let i = 0; i < N; i++){
    let curr = nums[i]

    if(curr % 2 == 0) multi2++
    if(curr % 3 == 0) multi3++
    if(curr % 4 == 0) multi4++
    if(curr % 5 == 0) multi5++
}

console.log(`${multi2} Multiplos de 2`)
console.log(`${multi3} Multiplos de 3`)
console.log(`${multi4} Multiplos de 4`)
console.log(`${multi5} Multiplos de 5`)