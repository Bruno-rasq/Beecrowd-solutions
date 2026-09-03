const fs = require("fs")
const input = fs.readFileSync("/dev/stdin", "utf8").split("\n").map(Number)
const n = input.shift()

const possibilidades= [
    0, 6, 12, 90, 360, 2040, 10080, 54810, 290640, 
    1588356, 8676360, 47977776, 266378112, 1488801600
]

for(let i = 0; i < n; i++){
    const curr = input[i]
    console.log(possibilidades[curr - 1])
}