// let input = require('fs').readFileSync("./test/stdin", 'utf8');
// let lines = input.split('\n');

console.log(" 1273 - Justifier ");

const input = `3
3 xYz Yxz
3 abc cba
6 ABCDEF CBAEDF`;

let lines = input.split('\n').map(el => Number(el));
let int = Number(lines.shift());