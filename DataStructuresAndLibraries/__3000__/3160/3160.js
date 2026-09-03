const fs = require("fs");
const input = fs.readFileSync("/dev/stdin", "utf8").split("\n");

const lista_atual = input.shift().split(" ")
const nova_lista  = input.shift().split(" ")
const amigo_indicado = input.shift()
let lista_atualizada = []

if (amigo_indicado != "nao" && lista_atual.includes(amigo_indicado)){
    for(const amigo of lista_atual){
        if (amigo == amigo_indicado){
            for(const novo_amigo of nova_lista){
                lista_atualizada.push(novo_amigo)
            }
        }
        lista_atualizada.push(amigo)
    }
} else {
    lista_atualizada = [...lista_atual, ...nova_lista]
}

console.log(lista_atualizada.join(" "))