const fs = require("fs");
const inputs = fs.readFileSync("/dev/stdin", "utf8").trim().split("\n");

const crypt = [
  ["GQaku", "0"],
  ["ISblv", "1"],
  ["EOYcmw", "2"],
  ["FPZdnx", "3"],
  ["JTeoy", "4"],
  ["DNXfpz", "5"],
  ["AKUgq", "6"],
  ["CMWhr", "7"],
  ["BLVis", "8"],
  ["HRjt", "9"]
];

const n = parseInt(inputs[0], 10);

for (let i = 1; i <= n; i++) {
  const frase = inputs[i];
  let incrypt = "";

  for (const char of frase) {
    if (char === " ") continue;

    for (const [letters, digit] of crypt) {
      if (letters.includes(char)) {
        incrypt += digit;
        break; // Evita múltiplas adições se o caractere existir em mais de uma string
      }
    }

    if (incrypt.length >= 12) break;
  }

  console.log(incrypt.slice(0, 12));
}