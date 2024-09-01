console.log(" 1072 - Interval 2 ");

const input = `4
14
123
10
-25`;

let lines = input.split('\n')
let int = Number(lines.shift())

let output = []
let IN = 0;
let OUT = 0;

for(let i = 0; i < int; i++){

    let number = Number(lines[i])

    if( number >= 10 && number <= 20){
        IN++
    } else {
        OUT++
    }
};

output.push(
    `${IN} in`,
    `${OUT} out`
)

console.log(output.join('\n'))