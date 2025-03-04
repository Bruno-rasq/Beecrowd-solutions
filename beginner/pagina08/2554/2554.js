const fs = require("fs");
const input = fs.readFileSync("/dev/stdin", "utf8").trim().split("\n");

const toArray = (str) => str.split(" ").map(Number);

function main() {
    let index = 0;
    
    while (index < input.length) {
        const [N_amigos, N_dias] = toArray(input[index++]);
        let datas_possiveis = [];

        for (let i = 0; i < N_dias; i++) {
            const linha = input[index++].split(" ");
            const data = linha[0];
            const votos = linha.slice(1).map(Number);

            if (votos.length === N_amigos && votos.every(v => v === 1)) {
                datas_possiveis.push(data);
            }
        }

        console.log(datas_possiveis.length > 0 ? datas_possiveis[0] : "Pizza antes de FdI");
    }
}

main();