console.log(" 2028 - Sequence of sequence");

const input = `0
1
2
3`;

let lines = input.trim().split('\n')
const soma = (num) => Math.floor(num * (num + 1) / 2)

let t = 1
while(lines.length){
    
    let N = Number(lines.shift())

    console.log(`Caso ${t++}: ${soma(N) + 1} numero${N === 0 ? '' : 's'}`)

    let resp = '0'
    for (let i = 0; i <= N; i++) {
        for(let j = 0; j < i; j++){
            resp += ` ${i}`
        }
    }

    console.log(`${resp}\n`)
}