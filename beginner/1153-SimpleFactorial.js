console.log(" 1153 - simple factorial");

const input = `4`;

let lines = input.split('\n');
let num = Number(lines[0]);

let fatorial = num ;

while (num > 1) { 
    num--;
    fatorial *= num;
}

console.log(Number(fatorial));