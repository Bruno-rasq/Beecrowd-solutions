const fs = require("fs")
const inputs = fs.readFileSync("/dev/stdin", "utf8").split("\n")
const numero_casos = Number(inputs.shift())

for(let i = 0; i < numero_casos; i++){
    const [pessoas, mililitros] = inputs.shift().split(" ").map(Number)
    const [b, B, H] = inputs.shift().split(" ").map(Number)
    
    const media = mililitros / pessoas
    const temp = (media * 3 * (B - b) / (Math.PI * H) + b ** 3) ** (1/3)
    const h = media * 3 / (Math.PI * (temp ** 2 + temp * b + b ** 2))
    
    console.log(h.toFixed(2))
}