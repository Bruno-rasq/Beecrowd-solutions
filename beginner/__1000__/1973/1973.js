const fs = require('fs')
const input = fs.readFileSync('/dev/stdin', 'utf8')
const lines = input.split('\n')
const n = Number(lines.shift())
const star = lines.shift().split(' ').map(Number)

let sheeps = 0
let attackedStars = new Array(n).fill(false)
let i = 0; 

const is_even = (n) => n % 2 == 0

while (i < n && i >= 0){

    if(star[i] > 0){
        sheeps++
        star[i]--
    }

    attackedStars[i] = true

    if(is_even(star[i] + 1)){
        i--
    } else {
        i++
    }

    if(i >= 0 && i < n && star[i] === 0) break
}

const countAttackedStars = attackedStars.filter(Boolean).length

const totalRemainingSheeps = stars.reduce((acc, curr) => acc + curr, 0)

console.log(`${countAttackedStars} ${totalRemainingSheeps}`)