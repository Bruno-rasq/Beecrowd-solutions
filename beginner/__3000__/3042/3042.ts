const fs = require("fs")
const input = fs.readFileSync("/dev/stdin", "utf8").trim().split('\n')

let index: number = 0
let n: number = Number(input[index++])

while (n > 0) {
     let posicaoAtual = 2;
     let contador = 0;

    for( let i = 0; i < n; i++){
        const linha = input[index++]

        if(linha == "0 1 1" && posicaoAtual != 1){
            contador += Math.abs(posicaoAtual - 1);
            posicaoAtual = 1;
        }
        else if(linha == "1 0 1" && posicaoAtual != 2){
            contador += Math.abs(posicaoAtual - 2);
            posicaoAtual = 2;
        }
        else if(linha == "1 1 0" && posicaoAtual != 3){
            contador += Math.abs(posicaoAtual - 3);
            posicaoAtual = 3;
        }
    }

    console.log(contador)
    n = Number(input[index++])
}