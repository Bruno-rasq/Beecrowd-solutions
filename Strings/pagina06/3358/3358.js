const fs = require('fs')
const input = fs.readFileSync('/dev/stdin', 'utf-8')
const lines = input.split('\n')
const vogais = ['a', 'e', 'i', 'o', 'u']
const n = Number(lines.shift())

for(let i = 0; i < n; i++){
    let is_hardest = false
    let auxiliar = lines.shift()
    let curr = aux.toUpperCase()

    for(let j = 0; j < curr.length; j++){
        let count = 0

        while(
            count < 3 && 
            j + count < curr.length && 
            !vogais.includes(curr[j + count])
        ){ count++ }

        if(count == 3){
            is_hardest = true
            break
        }
    }

    if(is_hardest){
        console.log(`${auxiliar} nao eh facil`)
    } else {
        console.log(`${auxiliar} eh facil`)
    }
}