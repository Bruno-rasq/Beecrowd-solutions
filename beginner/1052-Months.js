console.log(" 1052 - Months ");

const input = `4`;

let lines = input.split('\n');
let number = Number(lines.shift());

let months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

console.log(months[number - 1])