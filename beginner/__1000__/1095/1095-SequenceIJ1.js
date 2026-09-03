console.log(" 1095 - Sequence IJ 1 ");

const input = ``;
let lines = input.split('\n');

let i = 1
let j = 60

for(let n = 0; n <= j; n+=5){
    console.log(`I=${i} J=${j - n}`)
    i+=3
}