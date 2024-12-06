const fs = require("fs")
const input = fs.readFileSync("/dev/stdin", "utf8").split("\n")

for(let i = 0; i < input.length; i++){
    let n = parseInt(input[i])
    if(!isNaN(n)){
        let clonagem = Math.log2(n)
        console.log(clonagem)
    }
}