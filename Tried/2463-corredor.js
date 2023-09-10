console.log(" 2463 - corredor ");

const input = `10
50 42 -35 2 -60 5 30 -1 40 31`;

let lines = input.split('\n');

let int = Number(lines.shift());
let salas = lines[0].split(' ').map(item => {
    return Number(item)
});

let aux = [];

for ( let i = 0; i<salas.length - 2; i++){
    aux.push(Number(salas[i] + salas[i+1] + salas[i+2]))
}

let max = Math.max.apply(null, aux);

console.log(max)
