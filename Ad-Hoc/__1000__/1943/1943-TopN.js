console.log(" 1943 - top N");

const input = `7`;

let lines = input.split('\n');

let pos = Number(lines[0]);

if( pos == 1){
    console.log("Top 1");
} else if ( pos >= 2 && pos <= 3){
    console.log("Top 3");
} else if ( pos >= 3 && pos <= 5){
    console.log("Top 5");
} else if ( pos >= 5 && pos <= 10){
    console.log("Top 10");
} else if ( pos >= 10 && pos <= 25){
    console.log("Top 25");
} else if ( pos >= 25 && pos <= 50){
    console.log("Top 50");
} else if ( pos >= 50 && pos <= 100){
    console.log("Top 100");
};