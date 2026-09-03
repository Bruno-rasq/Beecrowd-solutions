console.log(" 1933 - tri-du ");

const input = `10 7`;

let lines = input.split(' ');
let numbers = lines.map(item => item * 1);

console.log(Math.max(...numbers));