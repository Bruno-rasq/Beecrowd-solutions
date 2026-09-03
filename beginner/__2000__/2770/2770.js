const fs = require("fs")
const input = fs.readFileSync("/dev/stdin", "utf8").trim().split('\n')

let index = 0;

while(index < input.length){

    const [larguraPlaca, alturaPlaca, qnt] = input[index++].split(' ').map(Number)
    const areaPlaca = larguraPlaca * alturaPlaca

    for(let i = 0; i < qnt; i++){
        const [larguraPdc, alturaPdc] = input[index++].split(' ').map(Number)
        
        const cabeNormal = larguraPdc <= alturaPlaca  && alturaPdc <= larguraPlaca
        const cabeRotacionado = larguraPdc <= larguraPlaca && alturaPdc <= alturaPlaca

        if(!cabeNormal && cabeRotacionado){
            console.log("Nao")
            continue
        }

        const areaPDc = larguraPdc * alturaPdc
        console.log(areaPDc <= areaPlaca ? "Sim" : "Nao")
    }
}
