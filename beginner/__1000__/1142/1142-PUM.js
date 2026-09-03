console.log(" 1142 - PUM ");

const input = `7`;

let lines = input.split('\n');
let int = Number(lines.shift());
let a = 1
let b = a + 1
let c = a + 2
let output = []

for(let i = 0; i < int; i++){
    output.push(
        `${a} ${b} ${c} PUM`
    )
    a+=4
    b+=4
    c+=4
};

console.log(output.join('\n'))