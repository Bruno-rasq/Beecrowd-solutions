console.log(" 1259 - Even and Odd ");

const input = `10
4
32
34
543
3456
654
567
87
6789
98`;

let lines = input.split('\n');
let int = Number(lines.shift());

let Even = [];
let Odd = [];

//verificando quais valores são pares e quais são impares
for ( let i = 0; i<int; i++ ){

    if(lines[i] % 2 == 0){
        Even.push(Number(lines[i]))

    } else if(lines[i] % 2 !== 0){
        Odd.push(Number(lines[i]))
    };

};

//ordenando os arrays, pares em crescente e impares em decrescente
function crescent(a, b) {
    return a - b;
};
function decrescent(a, b) {
    return b - a;
};

Even.sort(crescent);
Odd.sort(decrescent);


// inisrindo todos os items dos dois arrays em um  array de resposta
let response = [];

for(n in Even){
    response.push(Even[n])
};
for(n in Odd){
    response.push(Odd[n])
};

// exibindo resultado
for ( n in response ){
    console.log(response[n])
};