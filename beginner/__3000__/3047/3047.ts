const fs = require("fs")
const input = fs.readFileSync("/dev/stdin", "utf8")
const [mr_monica_ages, children_1, children_2] = input.split('\n').map(Number)
const children_3 = mr_monica_ages - (children_1 + children_2)

let eldest = children_1

if(children_2 > eldest){ eldest = children_2 }
if(children_3 > eldest){ eldest = children_3 }

console.log(eldest)