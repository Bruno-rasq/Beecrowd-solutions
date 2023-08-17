let n = 675;

let cen = Math.floor(n / 100);
let rest100 = n % 100;

let cin = Math.floor(rest100 / 50);
let rest50 = rest100 %50;

let vin = Math.floor(rest50 / 20);
let rest20 = rest50 % 20;

let dez = Math.floor(rest20 / 10);
let rest10 = rest20 % 10;

let cinco = Math.floor(rest10 / 5);
let rest5 = rest10 % 5;

let dois = Math.floor(rest5 / 2);
let rest2 = rest5 % 2;

let um = Math.floor(rest2 / 1);

console.log(n);
console.log(`${cen.toFixed(0)} notas(s) de R$ 100,00`);
console.log(`${cin.toFixed(0)} notas(s) de R$ 50,00`);
console.log(`${vin.toFixed(0)} notas(s) de R$ 20,00`);
console.log(`${dez.toFixed(0)} notas(s) de R$ 10,00`);
console.log(`${cinco.toFixed(0)} notas(s) de R$ 5,00`);
console.log(`${dois.toFixed(0)} notas(s) de R$ 2,00`);
console.log(`${um.toFixed(0)} notas(s) de R$ 1,00`);

console.log(rest100, rest50, rest20, rest10, rest5, rest2)