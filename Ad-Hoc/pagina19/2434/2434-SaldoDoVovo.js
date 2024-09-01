console.log(" 2434 - Saldo do vovo ");

const input = `3 1000
100
-800
50`;

let lines = input.split('\n');

let data = lines.shift().split(' ');
let [ dias, saldoInicial ] = data;

dias = Number(dias);
saldoInicial = Number(saldoInicial);

let resp = [];

for(let i = 0; i < dias; i++){


    let current = Number(lines[i]);
    let currentValue = saldoInicial + current;

    saldoInicial = currentValue;

    resp.push(currentValue)
};

let min = Math.min(...resp);

console.log(min);