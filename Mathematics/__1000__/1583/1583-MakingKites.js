console.log(" 1583 - Making kites ");

const input = `4
10 20
20 14
10 100
100 100`;

let lines = input.split('\n');
let int = Number(lines.shift());

for ( let i = 0; i < int; i++ ){

    let data = lines[i].split(' ')
    let [ D, d ] = data;
    D = Number(D)
    d = Number(d)

    let area = Math.trunc((D * d) / 2);

    console.log(`${area.toFixed(0)} cm2`)
};