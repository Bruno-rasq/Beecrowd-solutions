
const fs = require("fs")
const input = fs.readFileSync("/dev/stdin", "utf8").split("\n")
const [volume_inicial, qnt_alteracoes] = input.shift().split(" ").map(Number)
const alteracoes = input.shift().split(" ").map(Number)
const vol_min = 0; const vol_max = 100;

let vol_atual = volume_inicial;
for(let i = 0; i < qnt_alteracoes; i++){
    let variacao = alteracoes[i]
    let novo_vol = Math.max(vol_min, Math.min(vol_max, vol_atual + variacao))
    vol_atual = novo_vol
}

console.log(vol_atual)