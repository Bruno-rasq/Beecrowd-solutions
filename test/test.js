let A = 3.0;
let B = 4.0;
let C = 5.2;

let PI = 3.14159;

let AreaTring = (A * C) / 2.0;
let circle = PI * Math.pow(C, 2);
let trapezium = ((A + B) * C) / 2.0;
let square = Math.pow(B, 2);
let retangle = A * B;

console.log(`TRIANGULO: ${AreaTring.toFixed(3)}`);
console.log(`CIRCULO: ${circle.toFixed(3)}`);
console.log(`TRAPEZIO: ${trapezium.toFixed(3)}`);
console.log(`QUADRADO: ${square.toFixed(3)}`);
console.log(`RETANGULO: ${retangle.toFixed(3)}`);