console.log(" 1589 - Bob Conduit ");

const input = `3
1 1
2 8
8 2`;

let lines = input.split('\n');
let int = Number(lines.shift());

for ( let i = 0; i < int; i++ ){

    let data = lines[i].split(' ');
    let [ n1, n2 ]= data;
    n1 = Number(n1)
    n2 = Number(n2)

    console.log(n1 + n2);
};