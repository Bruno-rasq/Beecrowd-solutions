const fs = require("fs")
const input = fs.readFileSync("/dev/stdin", "utf8").split("\n").map(Number)

let tempo_seg = input.shift()
while (tempo_seg != 0) {
    let ale = Math.ceil(7 * tempo_seg / 90)
    let bra = Math.floor(tempo_seg / 90)

    console.log(`Brasil ${bra} x Alemanha ${ale}`)
    tempo_seg = input.shift()
}
