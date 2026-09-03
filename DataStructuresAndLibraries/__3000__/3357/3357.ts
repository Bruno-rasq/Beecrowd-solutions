import * as  fs from "fs"

const input = fs.readFileSync("/dev/stdin", "utf8").split("\n")

let [qnt_amigos, litros, refil] = input[0].split(" ").map(Number)
let lista_amigos = input[1].split(" ")
let index = 0

while (litros > refil){
    litros -= refil
    index = (index + 1) % qnt_amigos
}

const rico = lista_amigos[index]
console.log(`${rico} ${litros.toFixed(1)}`)