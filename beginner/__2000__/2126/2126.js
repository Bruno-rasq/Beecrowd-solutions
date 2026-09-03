const fs = require("fs");
const input = fs.readFileSync("/dev/stdin", "utf8").trim().split("\n");

let c = 1;
for (let i = 0; i < input.length; i += 2) {
    const subseq = input[i];
    const linha = input[i + 1];

    // Verifica se tem um par completo de linhas
    if (subseq === undefined || linha === undefined) break;

    let qts = 0;
    let pos = 0;

    for (let j = 0; j <= linha.length - subseq.length; j++) {
        let eh_sub = true;
        for (let k = 0; k < subseq.length; k++) {
            if (linha[j + k] !== subseq[k]) {
                eh_sub = false;
                break;
            }
        }
        if (eh_sub) {
            qts += 1;
            pos = j + 1;
        }
    }

    console.log(`Caso #${c}:`);
    if (qts === 0) {
        console.log("Nao existe subsequencia");
    } else {
        console.log(`Qtd.Subsequencias: ${qts}`);
        console.log(`Pos: ${pos}`);
    }
    console.log("");

    c += 1;
}
