const fs = require("fs")
const input = fs.readFileSync("/dev/stdin", "utf8").split("\n")

function Matriz(str1, str2) {
    return Array.from({ length: str1.length + 1 }, () => Array(str2.length + 1).fill(0))
}

function logCommonSub(str1, str2) {
    let matriz = Matriz(str1, str2);
    let MC = 0; // maior comprimento
    let FMS = 0; // fim maior sequência

    for (let i = 1; i <= str1.length; i++) {
        for (let j = 1; j <= str2.length; j++) {
            if (str1[i - 1] === str2[j - 1]) {
                matriz[i][j] = matriz[i - 1][j - 1] + 1;

                if (matriz[i][j] > MC) {
                    MC = matriz[i][j];
                    FMS = i - 1;
                }
            }
        }
    }

    if (MC === 0) return 0;

    return str1.substring(FMS - MC + 1, FMS + 1).length;
}

// Processando a entrada
while (input.length >= 2) {
    const str1 = input.shift().trim();
    const str2 = input.shift().trim();
    console.log(logCommonSub(str1, str2));
}