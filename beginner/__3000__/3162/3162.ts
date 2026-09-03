const fs = require("fs")
const input = fs.readFileSync("/dev/stdin", "utf8").split("\n")

function calcDistancia(x1, y1, z1, x2, y2, z2){
    return Math.sqrt(
        Math.pow(x2 - x1, 2) +
        Math.pow(y2 - y1, 2) +
        Math.pow(z2 - z1, 2)
    )
}

const n = Number(input.shift())
const naves = input.slice(0, n).map(line => line.split(' ').map(Number))

for(let i = 0; i < n; i++){
    let [nax, nay, naz] = naves[i]
    let menorDistancia = Infinity

    for(let j = 0; j < n; j++){
        if(i !== j){
            let [npx, npy, npz] = naves[j]
            let distancia = calcDistancia(nax, nay, naz, npx, npy, npz)

            if(distancia < menorDistancia){
                menorDistancia = distancia
            }
        }
    }

    if(menorDistancia > 50){ console.log("B") }
    else if (menorDistancia > 20 && menorDistancia <= 50){ console.log("M")}
    else {console.log("A")}
}
