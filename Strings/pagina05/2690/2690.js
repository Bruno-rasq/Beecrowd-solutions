const fs = require("fs")
const input = fs.readFileSync("/dev/stdin", "utf8").split("\n")
const n = Number(input.shift())

// Transformando `codex` em um mapa para busca mais eficiente
const codexMap = new Map();
[
    ["GQaku", "0"], ["ISblv", "1"], ["EOYcmw", "2"],
    ["FPZdnx", "3"], ["JTeoy", "4"], ["DNXfpz", "5"],
    ["AKUgq", "6"], ["CMWhr", "7"], ["BLVis", "8"],
    ["HRjt", "9"]
].forEach(([chars, num]) => {
    for (const char of chars) {
        codexMap.set(char, num);
    }
});

const crypt = (char) => codexMap.get(char) || "";  // Evita `undefined`

for (let i = 0; i < n; i++) {
    let incryp = "";
    let line = input[i];
    let j = 0;

    while (j < line.length && incryp.length < 12) { // Evita acessar índice inválido
        const char = line[j++];
        if (char !== " ") {
            incryp += crypt(char);
        }
    }
    console.log(incryp);
}