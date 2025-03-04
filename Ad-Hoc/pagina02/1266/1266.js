const fs = require("fs");
const input = fs.readFileSync("/dev/stdin", "utf8").split("\n");

while(true){
    
    let n = Number(input.shift())
    if (n === 0) break;
    
    let z = 0
    let s = 0
    let i = 0
    let p = 0
    
    let postes = input.shift().split(" ").map(Number)
    for(const poste of postes){
        if (poste === 0 && i === 0){
            z++
            p++
        }
        else if (poste === 0 && i === 1){
            p++
        }
        
        if (poste === 1){
            i = 1
            s += Math.floor(p / 2)
            p = 0
        }
    }
    
    if (p > 0){
        s -= Math.floor(z / 2)
        p += z
        s += Math.floor(p / 2)
    }
    
    console.log(s)
}