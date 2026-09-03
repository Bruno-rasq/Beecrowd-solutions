const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");

const wordplay = (palavra, i) => {
    let menor = palavra;
    let maior = palavra;
    let dupla = palavra + palavra; // para facilitar a rotação

    for (let j = 1; j < palavra.length; j++) {
        let rotacionada = dupla.substring(j, j + palavra.length);
        if (rotacionada < menor) menor = rotacionada;
        if (rotacionada > maior) maior = rotacionada;
    }

    console.log(`Caso ${i}: ${menor} ${maior}`);
};

let i = 1;
for (const palavra of input) {
    if (palavra === "*") break;
    wordplay(palavra, i);
    i++;
}
