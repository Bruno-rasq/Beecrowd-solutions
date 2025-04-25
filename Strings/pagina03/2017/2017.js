const input = require("fs").readFileSync("/dev/stdin", "utf8").split("\n")

const hamming_distance = (str1, str2) => {
    let distancie = 0
    for(let i = 0; i < str1.length; i++){
        if(str1[i] != str2[i]) distancie++
    }
    return distancie
}

const str1 = input.shift()
const k = Number(input.shift())

let indice = -1
let menor_distancia = Infinity

for(let i = 0; i < 5; i++){
    const str2 = input.shift()
    const distance = hamming_distance(str1, str2)

    if(distance < menor_distancia){
        menor_distancia = distance
        indice = i + 1
    }
}

console.log(indice)
console.log(menor_distancia <= k ? menor_distancia : -1)