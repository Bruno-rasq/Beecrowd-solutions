console.log(" 3342 - Keanu ");

const input = `3`;

let lines = input.split('\n');
let int = Number(lines.shift());

function KeanuChess(input){

   let CasasTotal = input * input;
   let B = 0
   let P = 0

   if(input % 2 == 0){
        B = CasasTotal / 2
        P = B
        console.log(`${B} casas brancas e ${P} casas pretas`)

   } else {
        B = (CasasTotal + 1) / 2
        P = B -1
        console.log(`${B} casas brancas e ${P} casas pretas`)

   }
    
};

KeanuChess(int);