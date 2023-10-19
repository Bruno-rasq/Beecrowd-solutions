console.log(" 1064 - Positives and Average ");

const input = `7
-5
6
-3.4
4.6
12`;

let lines = input.split("\n").map(num => Number(num));
let output = []
let positives = 0
let positiveSum = 0
let count = 0

for(n in lines){
    if(lines[n] > 0){
        positives++
        positiveSum+= lines[n]
        count++
    }
};

output.push(
    `${positives} valores positivos`,
    `${Number(positiveSum / count).toFixed(1)}`
)

console.log(output.join('\n'))