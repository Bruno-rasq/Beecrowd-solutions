const fs = require('fs')
const input = fs.readFileSync('/dev/stdin', 'utf-8')
const lines = input.split('\n')

const cases = Number(lines.shift())

for(let i = 0; i < cases; i++){

    let len = Number(lines.shift())
    let vet = lines.shift().split(' ').map(Number)
    let count = 0

    //implementando o algoritmo de bubble sort
    for(let j = 0; j < len - 1; j++){
        for(let k = 0; k < len - j - 1; k++){

            //swapping
            if(vet[k] > vet[k + 1]){
                count++
                let temp = vet[k]
                vet[k] = vet[k + 1]
                vet[k + 1] = temp
            }
        }
    }

    console.log(`Optimal train swapping takes ${count} swaps.`)
}