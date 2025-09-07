const fs = require("fs")
const input = fs.readFileSync("/dev/stdin", "utf8")
const [x1, y1, x2, y2] = input.split(' ')

const distance_manhattan = Math.abs(x1 - x2) + Math.abs(y1 - y2)

console.log(distance_manhattan)