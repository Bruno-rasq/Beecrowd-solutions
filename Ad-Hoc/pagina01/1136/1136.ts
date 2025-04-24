const fs = require("fs")
const input = fs.readFileSync("/dev/stdin", "utf8").split("\n")

const toArray = (str: string): number[] => str.split(" ").map(Number)

let i = 0
while(true){
    
    let [N, B] = toArray(input[i])
    if(N === 0 && B === 0)break

    const bolas = toArray(input[i + 1])
    const possibilidades = new Set()
    possibilidades.add(0)

    for(let i = 0; i < B; i++){
        for(let j = i + 1; j < B; j++){
            possibilidades.add(Math.abs(bolas[i] - bolas[j]))
        }
    }

    console.log(possibilidades.size == N + 1 ? 'Y' : 'N')
    i += 2
}