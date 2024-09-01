console.log(" 3465 - Cimba ");

const input = `7 8 9`;

let lines = input.split('\n');
let [ A, B, C ] = lines.shift().split(' ').map(el => Number(el));

let p = (A + B + C) / 2;
let  area = Math.sqrt(p * ((p - A) * (p - B) * (p - C)))

console.log(`${area.toFixed(3)} m2`)