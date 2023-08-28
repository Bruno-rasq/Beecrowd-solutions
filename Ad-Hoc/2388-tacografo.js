console.log(" 2388 - tacografo ");

const input = `3
10 0
55 12
75 120`;

let lines = input.trim().split('\n');
let int = Number(lines.shift());

let response = 0;

for(let i = 0; i < int; i++){

    let data = lines[i].split(' ');
    let [ velocidade, tempo ] = data;

    response += Number(velocidade) * Number(tempo);

};

console.log(response);