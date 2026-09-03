const datas = require("fs").readFileSync("/dev/stdin", "utf8")
const inputs = datas.split("\n")

inputs.pop()

while(inputs.length > 0){
    
    const [n, m] = inputs.shift().split(" ").map(Number)
    
    let X = undefined
    let Y = undefined
    
    for(let i = 0; i < n; i++){
        const linha = inputs.shift().split(" ").map(Number)
        for(let j = 0; j < m; j++){
            if(linha[j] == 1) X = [i, j]
            if(linha[j] == 2) Y = [i, j]
        }
    }
    
    const dist = Math.abs(X[0] - Y[0]) + Math.abs(X[1] - Y[1])
    console.log(dist)
}