console.log(" 1070 - Six Odd Numbers ");

const input = `7`;

let lines = input.split('\n');

let num = Number(lines.shift())
let odds = []
let int = 0

while(int < 6){

    if(num % 2 != 0){
        odds.push(num)
        int++
    }
    num = num + 1

}

console.log(odds.join('\n'))