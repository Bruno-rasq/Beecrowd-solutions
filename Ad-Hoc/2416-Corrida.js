console.log(" 2416 - Corrida ");

const input = `918 76`;

let lines = input.split(' ');

let numbers = lines.map(item => item * 1);
let [n1, n2] = numbers;

console.log(n1 % n2);