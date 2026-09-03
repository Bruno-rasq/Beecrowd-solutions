console.log(" 1332 - one two three ");

const input = `20
owe
onw
thrne
owe
one
threw
owe
nhree
too
nne
thren
tne
two
too
throe
oee
tww
thtee
ooe
ont`;

let lines = input.split('\n');
let int = Number(lines.shift());
const um = "one";

for(let i = 0; i < int; i++){
    let palavra = lines.shift();

    if(palavra.length === 5) console.log(3);

    else{
        let semelhancas = palavra.trim().split('').map((x, i) => [palavra[i], um[i]]).reduce((acc, cur) => (cur[0] === cur[1]) ? acc + 1 : acc, 0);
        if(semelhancas > 1) console.log(1);
        else                console.log(2);
    }
};