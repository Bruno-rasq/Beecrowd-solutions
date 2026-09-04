console.log(" 2328 - chocolate ");

const input = `5
2 2 2 3 3`;

let lines = input.split('\n');
let int = Number(lines.shift());
let parts = lines[0].split(' ').map(elem => Number(elem))

let output = 0
for(let i = 0; i < parts.length; i++){
    output+= parts[i]
}

console.log(output - int)