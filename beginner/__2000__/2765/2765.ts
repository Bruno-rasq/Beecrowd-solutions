const datas = require("fs").readFileSync("/dev/stdin", "utf8")
const frases = datas.split("\n")

frases.pop()

for(const frase of frases){
    const[a, b] = frase.split(",")
    console.log(a)
    console.log(b)
}