const fs = require("fs");
const input = fs.readFileSync("/dev/stdin", "utf8").split("\n");
let palavra_corrente = input.shift();

let memoria = {};

const permutacao_sem_repeticoes = (palavra) => {
    if (!palavra) return 0;

    const tamanho = palavra.length;
    let psr = 1;
    for (let i = tamanho; i >= 1; i--) {
        psr *= i; 
    }
    
    if (!(palavra in memoria)) memoria[palavra] = psr;

    return psr;
};

while (palavra_corrente !== "0") {
    palavra_corrente = palavra_corrente.trim();
    if (palavra_corrente === "0") break;

    if (palavra_corrente in memoria) {
        console.log(memoria[palavra_corrente]);
    } else {
        const permut = permutacao_sem_repeticoes(palavra_corrente);
        console.log(permut);
    }

    palavra_corrente = input.shift();
}