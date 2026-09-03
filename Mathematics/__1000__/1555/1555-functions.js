console.log(" 1555 - Functions ");

const input = `6
5 3
2 30
2 100
30 20
15 5
30 2`;

let lines = input.split('\n');
let int = Number(lines.shift());

// r(x, y) = (3x)² + y²
// b(x, y) = 2(x²) + (5y)²
// c(x, y) = -100x + y³.

for (let i = 0; i < int; i++){
    let data = lines[i].split(' ')
    let [ x, y ] = data;
    x = Number(x)
    y = Number(y)

    let FunctionRafael = (Math.pow((3*x), 2)) + (Math.pow(y,2));
    let functionBeto = (2 * Math.pow(x, 2)) + (Math.pow((5*y), 2));
    let functionCarlos = (-100 * x) + (Math.pow(y, 3));

    let aux = [];
    let names = ['Rafael', 'Beto', 'Carlos'];

    aux.push(FunctionRafael)
    aux.push(functionBeto)
    aux.push(functionCarlos)

    let max = Math.max(...aux);

    console.log(`${names[aux.indexOf(max)]} ganhou`)
};