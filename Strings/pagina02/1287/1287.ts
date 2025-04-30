const inputs = require("fs").readFileSync("/dev/stdin", "utf8").split("\n");
const valor_maximo = 2147483647;

inputs.pop(); // Remove a última linha vazia

for (const input of inputs) {
    let num = "";
    let is_valid = true;

    for (let i = 0; i < input.length; i++) {
        const ch = input[i];

        if (ch >= '0' && ch <= '9') {
            num += ch;
        } else if (ch === 'o' || ch === 'O') {
            num += '0';
        } else if (ch === 'l') {
            num += '1';
        } else if (ch === ' ' || ch === ',') {
            continue;
        } else {
            is_valid = false;
            break;
        }
    }

    const erro = num === "" || Number(num) > valor_maximo;
    console.log(is_valid && !erro ? String(Number(num)) : "error");
}
