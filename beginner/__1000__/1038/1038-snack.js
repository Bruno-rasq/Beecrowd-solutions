const fs = require('fs')
const input = fs.readFileSync('/dev/stdin', 'utf-8')
const [code, qnt] = input.split(' ').map(Number);

let menu = [4.00, 4.50, 5.00, 2.00, 1.50];
let total = menu[code-1] * qnt;

console.log(`Total: R$ ${total.toFixed(2)}`);