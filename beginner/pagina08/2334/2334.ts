const fs = require("fs")
const input = fs.readFileSync("/dev/stdin", "utf8").split("\n")

for(let i = 0; i < input.length; i++){

    let n_patinhos = BigInt(input[i])

    if(n_patinhos == BigInt(-1)) break
    
    console.log(n_patinhos > 0 ? (n_patinhos - BigInt(1)).toString() : 0)
}
