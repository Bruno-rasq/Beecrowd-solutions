const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const HORSEDELTA = [[-2,-1] , [-2, 1], [-1, -2], [-1, 2], [1, -2], [1, 2], [2, -1], [2,1]];
const PAWNDELTA = [[-1, -1], [-1, 1]];

let t = 0;
while(true){

    const horse = input.shift();
    if(horse == "0") break;

    const hx = horse.charCodeAt(0) - 49; // 49 -> ascii de '1'
    const hy = horse.charCodeAt(1) - 97; // 97 -> ascii de 'a'

    let dangerouspos = new Set();
    for(let i = 0; i < 8; i++){
        const pawn = input.shift();
        const px = pawn.charCodeAt(0) - 49; // 49 -> ascii de '1'
        const py = pawn.charCodeAt(1) - 97; // 97 -> ascii de 'a'
        for(const delta of PAWNDELTA){
            const npx = delta[0] + px;
            const npy = delta[1] + py;
            if(npx < 0 || npx > 7 || npy < 0 || npy > 7) continue;
            dangerouspos.add(`${npx} ${npy}`);
        }
    }

    let ans = 0;
    for(const delta of HORSEDELTA){
        const nhx = hx + delta[0];
        const nhy = hy + delta[1];
        if(nhx < 0 || nhx > 7 || nhy < 0 || nhy > 7) continue;
        if(dangerouspos.has(`${nhx} ${nhy}`)) continue;
        ans++;
    }

    console.log(`Caso de Test #${++t}: ${ans} movimento(s).`);
}