const fs = require("fs")
const input = fs.readFileSync("/dev/std", "utf8").trim().split('\n').map(Number)

let pares = []
let impares = []

for(let i = 0; i < 15; i++){
    const curr = input[i];
    
    if(curr % 2 === 0){
        pares.push(curr)
        if(pares.length === 5){
            for(let j = 0; j < pares.length; j++){
                console.log(`par[${j}] = ${pares[j]}`)
            }
            pares = []
        }
       
    }
    else {
        impares.push(curr)
        if(impares.length === 5){
            for(let j = 0; j < impares.length; j++){
                console.log(`impar[${j}] = ${impares[j]}`)
            }
            impares = []
        }
    }
}

for(let i = 0; i < impares.length; i++){
    console.log(`impar[${j}] = ${impares[j]}`)
}

for(let i = 0; i < pares.length; i++){
    console.log(`par[${j}] = ${pares[j]}`)
}