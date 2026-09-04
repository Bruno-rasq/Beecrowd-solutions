const fs = require('fs')
const input = fs.readFileSync('/dev/stdin', 'utf-8')
const n = Number(input) - 1;

type Crianca = {crianca: string, mao: boolean}

let index = 0;
let criancas: Crianca[] = [
    {crianca: "joao", mao: true},
    {crianca: "joao", mao: true},
]

const novaCrianca = (indice: number): void => {
    criancas.push({crianca: `c${indice}`, mao: true})
    criancas.push({crianca: `c${indice}`, mao: true})
}

const removerCrianca = (indice: number): void => {
    criancas.splice(indice, 1)
}

for(let i = 0; i < n; i++){
    novaCrianca(i + 2);
}

while(criancas.length > 1){
    index = (index + 28) % criancas.length
    removerCrianca(index)
}

console.log(criancas[0].crianca == "joao" ? "vai ganhar" : "nao vai ganhar")