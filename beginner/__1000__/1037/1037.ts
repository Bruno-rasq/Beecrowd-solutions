const fs = require('fs')
const input = fs.readFileSync('/dev/stdin', 'utf-8')
const lines = input.split('\n')

let Num = Number(lines[0]);

if(Num < 0 ){
    console.log("Fora de intervalo")

} else if ( Num >= 0 && Num <= 25 ){
    console.log("Intervalo [0,25]")

} else if ( Num >= 25 && Num <= 50 ){
    console.log("Intervalo (25,50]")

} else if( Num >= 50 && Num <= 75 ){
    console.log("Intervalo (50,75]")

} else if ( Num >= 75 && Num <= 100 ){
    console.log("Intervalo (75,100]")

} else if ( Num > 100 ){
    console.log("Fora de intervalo")
};