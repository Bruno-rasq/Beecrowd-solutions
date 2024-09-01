let time = Number(lines[0]);
let kmh = Number(lines[1]);

let response = ((time * kmh) / 12);
console.log(response.toFixed(3));