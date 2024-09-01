console.log(" 2061 - Closing tabs");

const input = `1 1
clicou`;

let lines = input.split('\n');

let inf = lines.shift().split(' ');
let [ pags , actions ] = inf;
pags = Number(pags);
actions = Number(actions);

let count = pags;

for ( let i = 0; i < actions; i++){
    if(lines[i] == 'fechou'){
        count += 1
    } else if ( lines[i] == 'clicou'){
        count -= 1
    }
};

console.log(count);