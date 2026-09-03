const fs = require("fs");
const input = fs.readFileSync("/dev/stdin", "utf8").trim().split("\n");

while (input.length > 0) {
    const header = input.shift();
    if (!header) break; // Evita processar linhas vazias
    const [total_palavras, max_linhas, max_chars] = header.split(" ").map(Number);
    const conto = input.shift().split(" ");

    let qnt_paginas = 0;
    let i = 0;

    while (i < conto.length) {
        let linhas = 0;
        while (linhas < max_linhas && i < conto.length) {
            let linha_len = 0;
            while (i < conto.length) {
                const palavra = conto[i];
                if (linha_len === 0) {
                    if (palavra.length <= max_chars) {
                        linha_len = palavra.length;
                        i++;
                    } else {
                        break;
                    }
                } else if (linha_len + 1 + palavra.length <= max_chars) {
                    linha_len += 1 + palavra.length;
                    i++;
                } else {
                    break;
                }
            }
            linhas++;
        }
        qnt_paginas++;
    }

    console.log(qnt_paginas);
}
