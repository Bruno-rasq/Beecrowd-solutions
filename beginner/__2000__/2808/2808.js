const fs = require("fs")
const input = fs.readFileSync("/dev/stdin", "utf8").split(" ")
const [posicao_inicial, posicao_desejada] = input

const deslocamentos = [[2, 1], [1, 2], [-1, 2], [-2, 1], [-2, -1], [-1, -2], [1, -2], [2, -1]]
const colunas = {"a": 1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h": 8}

const jogadaPossivel = (pi, pf) => {

    let coluna = colunas[pi[0]]
    let linha = Number(pi[1])

    for(const pos of deslocamentos){
        let nova_coluna = coluna + pos[0]
        let nova_linha = linha + pos[1]

        if(nova_coluna == colunas[pf[0]] && nova_linha == Number(pf[1])){
            return true
        }
    }

    return false
}

console.log(jogadaPossivel(posicao_inicial, posicao_desejada) ? "VALIDO" : "INVALIDO")