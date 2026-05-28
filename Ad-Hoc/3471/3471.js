const input = require('fs').readFileSync('/dev/stdin', 'utf8');
const [x, y] = input.split(" ").map(Number);

const GCD = (a, b) => {
    if(b == 0) return a;
    return GCD(b, a % b);
}

console.log(GCD(x, y));