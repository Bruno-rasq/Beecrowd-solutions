const fs = require("fs")
const input = fs.readFileSync('/dev/stdin', "utf-8")
const [a, b] = input.split(' ').map(Number)

if(a === 0.0 && b === 0.0){console.log("Origem")}
else if (a == 0.0){console.log("Eixo Y");}
else if (b == 0.0){console.log("Eixo X");}
else if (b > 0.0 && a > 0.0){console.log("Q1");}
else if (b > 0.0 && a < 0.0){console.log("Q2");}
else if (b < 0.0 && a < 0.0){console.log("Q3");}
else if (b < 0.0 && a > 0.0){console.log("Q4");}