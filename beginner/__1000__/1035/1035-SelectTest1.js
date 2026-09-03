const { listenerCount } = require("events");
const fs = require("fs")
const input = fs.readFileSync("/dev/stdin", "utf-8")
let lines = input.split(' ');

let A = Number(lines[0])
let B = Number(lines[1])
let C = Number(lines[2])
let D = Number(lines[3])

if ( B > C && D > A && (C + D) > (A + B) && C >= 0 && D >= 0 && A % 2 == 0){
    console.log("Valores aceitos")
} else {
    console.log("Valores nao aceitos")
};