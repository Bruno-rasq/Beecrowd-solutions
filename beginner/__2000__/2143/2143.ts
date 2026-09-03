const fs = require("fs")
const input = fs.readFileSync("/dev/stdin", "utf8").split("\n").map(Number)

let t = input.shift()
while(t != 0){
    for(let i = 0; i < t; i++){
        const n = input.shift()
        console.log((n - 1) % 2 == 0 ? 2 * n - 1: 2 * n - 2 )
    }
    t = input.shift()
}