const fs = require("fs")
const input = fs.readFileSync("/dev/stdin", "utf8").split("\n").map(Number)
const n = input.shift()

let stickers = new Set()
let repeated_stickers = 0

for(let i = 0; i < n; i++){
    const sticker = input[i]
    const curr_lenght = stickers.size

    stickers.add(sticker)

    repeated_stickers += curr_lenght == stickers.size ? 1 : 0
}

console.log(stickers.size)
console.log(repeated_stickers)
