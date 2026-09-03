import * as fs from "fs"
const input: string[]= fs.readFileSync("/dev/stdin", "utf8").split("\n")

for(let i = 0; i < input.length; i++){
    let n: number = parseInt(input[i])
    if(!isNaN(n)){
        let clonagem: number = Math.log2(n)
        console.log(Math.floor(clonagem))
    }
}