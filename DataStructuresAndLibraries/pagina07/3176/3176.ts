const fs = require('fs')
const input = fs.readFileSync('/dev/stdin', 'utf-8')
const lines = input.split('\b')

const len = Number(lines.shift())
let gnomes = []

//caprturando os gnomes
for(let i = 0; i < len ; i++){
    let [nome, idade] = lines.shift().split(' ')
    gnomes.push([nome, Number(idade)])
}

const sortedgnomes = (list) => {
    return list.sort((a, b) => {
        if(a[1] === b[1]){
            return a[0].localeCompare(b[0]) // comparação alfabetica de nomes
        }
        return b[1] - a[1] // ordenação por ordem decrestente de idade
    })
}

const list = sortedgnomes(gnomes)

let time = 1
let v = len /3
let i = 0

while(true){
    console.log(`Time ${time}`)
    console.log(list[i][0], list[i][1])
    console.log(list[i + v][0], list[i + v][1])
    console.log(list[i + 2 * v][0], list[i + 2 * v][1])
    console.log()

    i++
    if(time == v) break
    time++
}