console.log(" 2454 - Flipper ");

const input = `1 0`;

let lines = input.split(' ');
let [ p, r ] = lines
p = Number(p)
r = Number(r)

if ( p == 0 ){
    console.log("C")
} else if ( p == 1 ){
    if( r == 1 ){
        console.log("A")
    } else if ( r == 0 ){
        console.log("B")
    }
};