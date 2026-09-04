console.log(" 2473 - loteria ");

const input = `34 55 77 12 23 99
5 3 77 55 42 34`;

let lines = input.split('\n');

let apostados = lines[0].split(' ');
let sorteados = lines[1].split(' ');


let count = 0;

for ( n in sorteados ){
    if(apostados.includes(sorteados[n]) == true){
        count++
    }
};

if(count < 3){
    console.log("azar")

} else if (count == 3){
    console.log("terno")

} else if (count == 4){
    console.log("quadra")

} else if (count == 5){
    console.log("quina")

} else if (count == 6){
    console.log("sena")
};