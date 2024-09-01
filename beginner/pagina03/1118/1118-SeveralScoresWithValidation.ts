const input = `-3.5
3.5
11.0
10.0
4
1
8.0
9.0
2`

// const input = require('fs').readFileSync('/dev/stdin', 'utf-8');
const lines = input.split('\n').map(Number)

function average(){

    let notas = []
    let stop = false

    while(!stop){
        let curr = Number(lines.shift())

        if(curr < 0 || curr > 10){
            console.log('nota invalida')
            continue
        }

        notas.push(curr)
        if(notas.length === 2) stop = true
    }

    let media = notas.reduce((acc, curr) => acc += curr) / 2
    console.log(`media = ${media.toFixed(2)}`)

}

function main() {

    average()
    while(lines.length){

        console.log('novo calculo (1-sim 2-nao)')
        let curr = Number(lines.shift())
        
        if(curr === 2){
            break
        }

        if(curr === 1){
            average()
        }
    }
}

main()