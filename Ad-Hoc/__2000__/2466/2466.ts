const fs = require("fs")
const input = fs.readFileSync('/dev/stdin', 'utf-8')
const lines = input.split('\n')

const N = Number(lines.shift())
const balls = String(lines.shift()).split(' ').map(Number)

const sinuca = (len: number, data: number[]) => {

    let balls = data
    let N = len

    while(N > 1){
        let newballs: number[] = []

        for (let i = 0; i < N; i++){
            newballs.push(balls[i] == balls[i+1] ? 1 : -1)
        }

        balls = newballs
        N = newballs.length
    }

    console.log(balls[0] == 1 ? "preta" : "branca")
}

sinuca(N, balls)