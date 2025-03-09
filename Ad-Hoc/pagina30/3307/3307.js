const fs  = require("fs")
const input = fs.readFileSync("/dev/stdin", "utf8").split("\n").map(Number)
const num_casos = input.shift()

const calcular_raio = (area) => Math.sqrt(area / (4 * 3.14))

for(let i = 0; i < num_casos; i++){
    let area = input[i]
    let raio = calcular_raio(area)

    if (raio < 12){
        let valor = area * 0.09
        console.log(`vermelho = R$ ${valor.toFixed(2)}`)
    }
    
    else if (raio >= 12 && raio <= 15){
        let valor = area * 0.07
        console.log(`azul = R$ ${valor.toFixed(2)}`)
    }
    
    else if (raio > 15){
        let valor = area * 0.05
        console.log(`amarelo = R$ ${valor.toFixed(2)}`)
    }
}