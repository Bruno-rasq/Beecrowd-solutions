const fs = require("fs");
const input = fs.readFileSync("/dev/stdin", 'utf-8');

let [reais, centavos] = input.split(".").map(Number);

// Converte tudo para centavos
reais = reais * 100 + centavos;

const notas: number[]  = [10000, 5000, 2000, 1000, 500, 200];
const moedas: number[] = [100,   50,   25,   10,   5,   1  ];

console.log("NOTAS:");
for (const nota of notas) {
    console.log(`${Math.floor(reais / nota)} nota(s) de R$ ${(nota / 100).toFixed(2)}`);
    reais %= nota;
}

console.log("MOEDAS:");
for (const moeda of moedas) {
    console.log(`${Math.floor(reais / moeda)} moeda(s) de R$ ${(moeda / 100).toFixed(2)}`);
    reais %= moeda;
}
