console.log(" 1042 - Simple Sort ");

const input = `7 21 -14`;

let lines = input.split(' ').map(el => Number(el));

let output = []
let orderList = [...lines].sort((a, b) => a - b)

output.push(
    orderList.join('\n'),
    '',
    lines.join('\n')
)

console.log(output.join('\n'))