import * as fs from "fs"
const input = fs.readFileSync("/dev/stdin", "utf8").trim().split("\n")
const casos = input.length / 2;

for(let i = 0; i < casos; i++){

    const jogadores = Number(input.shift())
    const doisTercos = jogadores * (2 / 3)
    const votos = input.shift().split(" ").map(Number)
    let votosImpeachment = 0

    for(let j = 0; j < jogadores; j++){
        votosImpeachment += votos[j] === 1 ? 1 : 0
    }

    console.log(votosImpeachment >= doisTercos ? "impeachment" : "acusacao arquivada")
}