import * as fs from "fs"
const input = fs.readFileSync("/dev/stdin", "utf8")
let lines = input.split(' ').map(el => Number(el));

let output = []
let orderList = [...lines].sort((a, b) => a - b)

output.push(
    orderList.join('\n'),
    '',
    lines.join('\n')
)

console.log(output.join('\n'))