console.log(" 1065 - Even Between five Numbers ");

const input = `7
-5
6
-4
12`;

let lines = input.split('\n');

let count = 0
for(let i = 0; i < 5; ++i){

    let num = Math.abs(lines.shift());
    count+= !(num % 2)

}

console.log(`${count} valores pares`)