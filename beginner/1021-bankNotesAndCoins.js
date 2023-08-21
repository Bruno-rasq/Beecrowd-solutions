
let n = input.split(" ").map(item => parseFloat(item));


let CEM = Math.floor(n / 100);

let CINQUENTA = Math.floor((n - (100 * CEM)) / 50);

let VINTE = Math.floor((n - (100 * CEM) - (50 * CINQUENTA)) / 20);

let DEZ = Math.floor((n - (100 * CEM) - (50 * CINQUENTA) - (20 * VINTE)) / 10);

let CINCO = Math.floor((n - (100 * CEM) - (50 * CINQUENTA) - (20 * VINTE) - (10 * DEZ)) / 5);

let DOIS = Math.floor((n - (100 * CEM) - (50 * CINQUENTA) - (20 * VINTE) - (10 * DEZ) - (5 * CINCO)) / 2);


let restCEM = n % 100;
let restCINQ = restCEM % 50;
let restVINT = restCINQ % 20;
let restDEZ = restVINT % 10;
let restCINC = restDEZ % 5;
let restDOIS = restCINC % 2;


let Coins = restDOIS * 100;

let Coin1 = Math.floor(Coins / 100);

let cent50 = Math.floor((Coins - (100 * Coin1)) / 50);

let cent25 = Math.floor((Coins - (100 * Coin1) - (50 * cent50)) / 25);

let cent10 = Math.floor((Coins - (100 * Coin1) - (50 * cent50) - (25 * cent25)) / 10);

let cent5 = Math.floor((Coins - (100 * Coin1) - (50 * cent50) - (25 * cent25) - (10 * cent10)) / 5);

let cent1 = Math.floor((Coins - (100 * Coin1) - (50 * cent50) - (25 * cent25) - (10 * cent10) - (5 * cent5)) / 1);

console.log("NOTAS:");
console.log(`${CEM.toFixed(0)} nota(s) de R$ 100.00`);
console.log(`${CINQUENTA.toFixed(0)} nota(s) de R$ 50.00`);
console.log(`${VINTE.toFixed(0)} nota(s) de R$ 20.00`);
console.log(`${DEZ.toFixed(0)} nota(s) de R$ 10.00`);
console.log(`${CINCO.toFixed(0)} nota(s) de R$ 5.00`);
console.log(`${DOIS.toFixed(0)} nota(s) de R$ 2.00`);

console.log("MOEDAS:");
console.log(`${Coin1.toFixed(0)} moeda(s) de R$ 1.00`);
console.log(`${cent50.toFixed(0)} moeda(s) de R$ 0.50`);
console.log(`${cent25.toFixed(0)} moeda(s) de R$ 0.25`);
console.log(`${cent10.toFixed(0)} moeda(s) de R$ 0.10`);
console.log(`${cent5.toFixed(0)} moeda(s) de R$ 0.05`);
console.log(`${cent1.toFixed(0)} moeda(s) de R$ 0.01`);

