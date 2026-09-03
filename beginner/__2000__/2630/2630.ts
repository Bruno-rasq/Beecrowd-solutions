import * as fs from "fs"
const input = fs.readFileSync("/dev/stdin", "utf8").split("\n")

const R = 0.30;
const G = 0.59;
const B = 0.11;

const OUTPUT = (caso: number, valor: number): void => console.log(`Caso #${caso}: ${valor}`)
const grayscale = (r: number, g: number, b: number): number => Math.trunc(R * r + G * g + B * b);
const minscale = (r: number, g: number, b: number): number => Math.min(r, g, b);
const maxscale = (r: number, g: number, b: number): number => Math.max(r, g, b);
const average = (r: number, g: number, b: number): number => Math.trunc((r + g + b) / 3);

const number_cases: number =  Number(input.shift())
 
for(let i = 1; i <= number_cases; i++){

    const type = input.shift()
    const [r, g, b] = String(input.shift()).split(' ').map(Number)
    let resultado = 0;

    if(type == "eye"){ resultado = grayscale(r, g, b); }
    if(type == "min"){ resultado = minscale(r, g, b); }
    if(type == "max"){ resultado = maxscale(r, g, b); }
    if(type == "mean"){ resultado = average(r, g, b); }

    OUTPUT(i, resultado)
}