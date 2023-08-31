console.log(" 2137 - The Library of Mr. Severino ");

const input = `3
1233
0015
0100`;

let lines = input.split('\n');
let int = Number(lines.shift());
lines = lines.sort();

for( let i = 0; i< int; i++){
    console.log(lines[i])
};