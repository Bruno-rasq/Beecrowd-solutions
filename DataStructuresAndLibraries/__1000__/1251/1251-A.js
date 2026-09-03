const inputs = require("fs").readFileSync("/dev/stdin", "utf8").split("\n")

let saidas = [];

inputs.pop()

for (const linha of inputs) {
    let freq = {};

    for (const char of linha) {
        const idx = char.charCodeAt();
        freq[idx] = (freq[idx] || 0) + 1;
    }

    let freqEntries = Object.entries(freq).map(([key, value]) => [parseInt(key), value]);

    freqEntries.sort((a, b) => {
        if (a[1] !== b[1]) {
            return a[1] - b[1]; // Frequência crescente
        } else {
            return b[0] - a[0]; // ASCII decrescente em empate
        }
    });

    const resultado = freqEntries.map(([ascii, count]) => `${ascii} ${count}`).join("\n");
    saidas.push(resultado);
}

console.log(saidas.join("\n\n"));