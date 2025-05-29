const fs = require("fs");
const input = fs.readFileSync("/dev/stdin", "utf8").split("\n");

for (let i = 0; i < input.length; i += 2) {
    
    const n = parseInt(input[i]);
    if (n === 0 || isNaN(n)) break;

    const arr = input[i + 1].trim().split(" ").map(Number);
    const freq = {};

    for (const num of arr) {
        freq[num] = (freq[num] || 0) + 1;
    }

    const impares = Object.keys(freq)
        .filter(key => freq[key] % 2 === 1)
        .map(Number)
        .sort((a, b) => a - b);

    console.log(impares.join(" "));
}