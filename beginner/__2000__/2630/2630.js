const fs = require("fs")
const input = fs.readFileSync("/dev/stdin", "utf8").split("\n")

const R = 0.30;
const G = 0.59;
const B = 0.11;

const OUTPUT = (caso, valor) => console.log(`Caso #${caso}: ${valor}`)
const grayscale = (r, g, b) => Math.trunc(R * r + G * g + B * b);
const minscale = (r, g, b) => Math.min(r, g, b);
const maxscale = (r, g, b) => Math.max(r, g, b);
const average = (r, g, b) => Math.trunc((r + g + b) / 3);

const number_cases =  Number(input.shift())
 
for(let i = 1; i <= number_cases; i++){
    const type = input.shift()
    const [r, g, b] = input.shift().split(' ').map(Number)
    let resultado = 0;

    if(type == "eye"){ resultado = grayscale(r, g, b); }
    if(type == "min"){ resultado = minscale(r, g, b); }
    if(type == "max"){ resultado = maxscale(r, g, b); }
    if(type == "mean"){ resultado = average(r, g, b); }

    OUTPUT(i, resultado)
}