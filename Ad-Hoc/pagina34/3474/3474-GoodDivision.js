console.log(" 3474 - Good division");

const input = `10.00 4`;
let [divisor, dividendo] = input.split(' ').map(item => Number(item));
let response = divisor / dividendo;

console.log(response.toFixed(2));