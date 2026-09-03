console.log(" 2840 - balloon++ ");

const input = `4 4000`;
let lines = input.split(' ');

let [ r, G ] = lines;
let pi = 3.1415;
r = Number(r);
G = Number(G);

let volume = ((4/3) * pi) * Math.pow(r, 3);
let resp = Math.floor(G / volume);

console.log(resp.toFixed(0));
