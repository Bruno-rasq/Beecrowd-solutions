console.log(" 2455 - gangorra");

const input = `30 100 60 50`;
const input2 = `40 40 38 60`;
const input3 = `35 80 35 75`;
// p1 c1 p2 c2

let lines = input.split(' ');
let [ p1, c1, p2, c2 ] = lines;

if((Number(p1)*Number(c1)) == (Number(p2)*Number(c2))){
    console.log(0)
} else if ((Number(p1)*Number(c1)) > (Number(p2)*Number(c2))){
    console.log(-1)
} else {
    console.log(1)
};