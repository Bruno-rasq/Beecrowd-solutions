import * as fs from "fs"

const input = fs.readFileSync("/dev/stdin", "utf8")
let [h1, m1,  h2, m2] = input.split(' ').map(Number)

if (h2 <= h1 && m2 <= m1){
    h2 = h2 + 24
}
else if (m2 <= m1){
    m2 = m2 + 60
    h2 = h2 - 1
}

let s1 = (h1 * 3600) + (m1 * 60) 
let s2 = (h2 * 3600) + (m2 * 60)

let tempo = s2 - s1
let hr = Math.floor(tempo / 3600)
let min = ((tempo - (hr * 3600)) / 60)

console.log(`O JOGO DUROU ${hr} HORA(S) E ${min} MINUTO(S)`)