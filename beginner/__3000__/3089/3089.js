const fs = require("fs")
const input = fs.readFileSync("/dev/std", "utf8")

while(true){

    const n = Number(input.shift())

    if(n === 0 ) break

    const presentes = input.shift().trim().split(' ').map(Number)

    let pares = []
    for(let i = 0; i < n; i++){
        pares.push(presentes[i] + presentes[2 * n - i - 1])
    }

    console.log(`${Math.max(...pares)} ${Math.min(...pares)}`)
}