const fs = require('fs')
const input = fs.readFileSync('/dev/stdin', 'utf-8').trim().split('\n')

while(input.length){

    let [totalVoluntarios, voluntariosRetornantes] = input.shift().split(' ').map(Number)

    if(totalVoluntarios === voluntariosRetornantes){
        console.log("*")
        input.shift()
        continue
    }

    let tagsRetornantes = new Set(input.shift().split(' ').map(Number))

    let tagsFaltantes = []
    for (let i = 0; i < totalVoluntarios; i++){
        if(!tagsRetornantes.has(i)){
            tagsFaltantes.push(i)
        }
    }

    console.log(tagsFaltantes.join(' ') + ' ')
}