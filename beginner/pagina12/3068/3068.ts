const fs = require("fs");
const input = fs.readFileSync("/dev/stdin", "utf8").trim().split("\n");

let i = 1;
let index = 0;

while (true) {
    let [x1, y1, x2, y2] = input[index++].split(" ").map(Number);
    
    if (x1 === 0 && y1 === 0 && x2 === 0 && y2 === 0) break;

    const n = Number(input[index++]);
    let meteoritos = 0;

    for (let j = 0; j < n; j++) {
        const [x, y] = input[index++].split(" ").map(Number);

        // Verifica se o meteoro caiu dentro ou sobre a borda da fazenda
        if (x1 <= x && x <= x2 && y2 <= y && y <= y1) {
            meteoritos++;
        }
    }

    console.log(`Teste ${i}`);
    console.log(meteoritos);
    i++;
}
