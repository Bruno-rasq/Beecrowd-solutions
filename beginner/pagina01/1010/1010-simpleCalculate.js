const fs = require('fs')
const input = fs.readFileSync('/dev/stdin', 'utf-8')
const lines = input.split('\n')

const [codigo1, quantidade1, preco1] = lines[0].split(' ');
const [codigo2, quantidade2, preco2] = lines[1].split(' ');

let total = (quantidade1 * preco1) + (quantidade2 * preco2);

console.log(`VALOR A PAGAR: R$ ${total.toFixed(2)}`);