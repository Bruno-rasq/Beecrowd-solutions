const fs = require('fs')
const input = fs.readFilSync('/dev/stdin', 'utf-8')
let lines = input.trim().split("\n")

lines.pop()

let contagemCidade = 0, count = 0
while(count < lines.length){

    let numeroDePessoas = parseInt(lines[count++])

    if(contagemCidade){ //adiciona uma linha em brtanco apenas depois se houver proximo cidade
        console.log('' )
    }

    //iniciando array de consumos com valores 0
    let consumos = new Array(201).fill(0)
    let [totalx, totaly] = [0, 0]

    for(let i = 0; i < numeroDePessoas; ++i){
        let [x, y] = lines[count++].split(' ').map(Number)

        if(x === 0) continue

        totalx += x
        totaly += y
        consumos[Math.floor(y / x)] += x
    }

    console.log(`Cidade# ${contagemCidade}:`)
    let output: string[] = []
    for(let i = 0; i < 201; ++i){
        if(consumos[i] > 0){
            output.push(`${consumos[i]}-${i}`)
        }
    }

    console.log(output.join(' '))

    if(totalx !== 0){
        let consumoMedio = Math.floor(100 * totaly / totalx) / 100
        console.log(`Consumo medio: ${consumoMedio.toFixed(2)} m3.`)
    }
}