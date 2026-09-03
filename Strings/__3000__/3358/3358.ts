const fs = require('fs')
const input = fs.readFileSync('/dev/stdin', 'utf-8')
const lines = input.split('\n')
const vogais = ['a', 'e', 'i', 'o', 'u']
const n = Number(lines.shift())

for(let i = 0; i < n; i++){

    let is_hardest = false
    let sobrenome = lines.shift()
    let count = 0

    for(let j = 0; j < sobrenome.length; j++){

        let letter = sobrenome[j].toLowerCase()

        if(!vogais.includes(letter)){
            count++
        } else {
            count = 0;
        }

        if(count == 3){
            is_hardest = true
            break
        }
    }

    if(is_hardest){
        console.log(`${sobrenome} nao eh facil`)
    } else {
        console.log(`${sobrenome} eh facil`)
    }
}