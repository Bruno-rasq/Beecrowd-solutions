console.log(" 1060 - Positive Numbers ");

const input = `7
-5
6
-3.4
4.6
12`;

let lines = input.split('\n').map(item => Number(item));
let count = 0;

for(n in lines){
    if(lines[n] > 0){
        count++
    }
}

console.log(`${count} valores positivos`)