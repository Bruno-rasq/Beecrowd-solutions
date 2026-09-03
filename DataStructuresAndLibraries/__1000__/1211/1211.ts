const fs = require("fs")
const inputs = fs.readFileSync("/dev/stdin", "utf8").split("\n")

let i = 0;
while (i < inputs.length) {
    const n = Number(inputs[i++]);
    if (!n || i + n > inputs.length) break;

    const numeros = inputs.slice(i, i + n);
    i += n;

    numeros.sort();

    let digitos_economizados = 0;
    for (let j = 1; j < n; j++) {
        const a = numeros[j], b = numeros[j - 1];
        const minLen = Math.min(a.length, b.length);
        for (let k = 0; k < minLen; k++) {
            if (a[k] !== b[k]) break;
            digitos_economizados++;
        }
    }

    console.log(digitos_economizados);
}