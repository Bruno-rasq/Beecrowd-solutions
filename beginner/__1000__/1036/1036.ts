const input = require("fs").readFileSync("/dev/stdin", "utf-8")
let [A, B, C] = input.split(' ').map(Number);

//x = (-b ± √(b² – 4ac)) / (2a) 
let delta = (B*B) - (4*A*C);

if (delta >= 0 && A !== 0){

    let r1 = (-B + Math.sqrt(delta)) / (2*A);
    let r2 = (-B - Math.sqrt(delta)) / (2*A);

    console.log(`R1 = ${r1.toFixed(5)}`)
    console.log(`R2 = ${r2.toFixed(5)}`)

} else {
    console.log("Impossivel calcular");
};