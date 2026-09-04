console.log(" 3058 - Supermercado ");

const input = `5
46.50 794
25.72 130
66.00 800
22.45 110
38.99 453`;

let lines = input.split('\n');
let supermarkets = Number(lines.shift());

let prices = []

for (let i = 0; i < supermarkets; i++){

    let data = lines[i].split(' ').map(i => Number(i))
    let [ bit, g ] = data;

    let Calc = ((1000 / g) * bit).toFixed(2);
    prices[i] = Calc
}

let response = Math.min(...prices.map(i => Number(i))).toFixed(2)

console.log(response)