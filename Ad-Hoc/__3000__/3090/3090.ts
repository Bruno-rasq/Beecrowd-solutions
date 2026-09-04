const fs = require("fs");
const input = fs.readFileSync("/dev/stdin", "utf8").trim().split("\n");

const [comprimento, largura, nsoldados] = input[0].split(" ").map(Number);

let hemisferio_a = 0;
let hemisferio_b = 0;

const coeficiente = largura / comprimento; // Pré-cálculo para evitar repetição

for (let i = 1; i <= nsoldados; i++) {
    const [coord_x, coord_y, poder] = input[i].split(" ").map(Number);
    
    if (coord_y > coeficiente * coord_x) {
        hemisferio_a += poder;
    } else {
        hemisferio_b += poder;
    }
}

console.log(`${hemisferio_a} ${hemisferio_b}`);