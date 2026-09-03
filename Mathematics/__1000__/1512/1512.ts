const input = require('fs').readFileSync('/dev/stdin', 'utf8');
const lines = input.split("\n");

const GCD = (a, b) => {
    if (b === 0) return a;
    return GCD(b, a % b);
}

const MMC = (a, b) => {
    if (a === 0 || b === 0) return 0;
    return (a * b) / GCD(a, b);
}

for (let i = 0; i < lines.length - 2; i++) {
    const [N, A, B] = lines[i].split(" ").map(Number);
    const ans =
        Math.floor(N / A) +
        Math.floor(N / B) -
        Math.floor(N / MMC(A, B));

    console.log(ans);
}