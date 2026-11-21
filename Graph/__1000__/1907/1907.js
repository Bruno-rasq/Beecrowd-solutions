const fs = require("fs");
const input = fs.readFileSync("/dev/stdin", "utf-8").trim();
const lines = input.split("\n");

const [height, width] = lines.shift().split(" ").map(Number);
let frame = lines.map(line => line.trim().split(""));

const bfs = (row, col) => {
    const deltax = [-1, 1, 0, 0];
    const deltay = [0, 0, -1, 1];

    let queue = [{x: row, y: col}];
    let head = 0;

    // MARCA O PIXEL INICIAL COMO VISITADO
    frame[row][col] = "O";

    while(head < queue.length){
        let curr = queue[head];
        head++;

        for(let i = 0; i < 4; i++){
            let nx = curr.x + deltax[i];
            let ny = curr.y + deltay[i];

            if(
                nx >= 0 && nx < height &&
                ny >= 0 && ny < width &&
                frame[nx][ny] == "."
            ){
                // MARCA ANTES DE INSERIR NA FILA
                frame[nx][ny] = "O";

                queue.push({x: nx, y: ny});
            }
        }
    }
};

const main = () => {
    let coloredAreas = 0;

    for(let row = 0; row < height; row++){
        for(let col = 0; col < width; col++){
            if(frame[row][col] == "."){
                coloredAreas++;
                bfs(row, col);
            }
        }
    }

    console.log(coloredAreas);
};

main();
