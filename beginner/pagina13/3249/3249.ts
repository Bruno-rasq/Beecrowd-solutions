import * as fs from "fs"
const input = fs.readFileSync("/dev/stdin", "utf8").split("\n")
const n = Number(input.shift())

let wins = 0

for(let i = 0; i < n; i++){
    const curr = String(input.shift())
    if(!curr.includes("CD")){
        wins++
    }
}

console.log(wins)