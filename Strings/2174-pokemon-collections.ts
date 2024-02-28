const input = `7
Charmander
Caterpie
Pidgeot
Rattata
Zubat
Zubat
Zubat`

const lines = input.split('\n')

// const input = require('fs').readFileSync('/dev/stdin', 'utf8');
// const lines = input.split('\n')


function main() {

    let int = Number(lines.shift())
    let bag = new Set()

    for(let i = 0; i < int; i++){
        bag.add(lines[i])
    }

    console.log(`Falta(m) ${ 151 - bag.size} pomekon(s).`)
}

main()