console.log(" 2936 - how much cassava? ");

const input = `5
4
3
2
1`;

let lines = input.split('\n');

let a = Number(lines[0])
let b = Number(lines[1])
let c = Number(lines[2])
let d = Number(lines[3])
let e = Number(lines[4])


let response = (a * 300) + (b * 1500) + (c * 600) + (d * 100) + (e * 150) + 225;
console.log(response);