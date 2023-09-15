console.log(" 1038 - snack ");

const input = `3 2`;

let lines = input.split(' ');

let code = Number(lines[0]);
let qnt = Number(lines[1]);

let menu = [4.00, 4.50, 5.00, 2.00, 1.50];

let total = ( menu[code-1] ) * qnt;


console.log(`Total: R$ ${total.toFixed(2)}`);