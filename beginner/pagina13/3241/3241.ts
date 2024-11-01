const fs = require("fs")
const input = fs.readFileSync("/dev/stdin", "utf8")
const lines = input.split("\n")
const n = Numbwer(lines.shift())

for(let i = 0; i < n; i++){
    let curr = lines.shift()

    if(curr === "P=NP"){
        console.log("skipped")
        continue
    }

    let [a, b] = curr.trim().split("+")
    a= Number(a)
    b= Number(b)

    console.log(a + b)
}