console.log(" 1144 - logical sequences");

const input = `5`;
let lines = input.split('\n');
let int = Number(lines[0]);

for (let i = 1; i< int+1; i++){

    let aux = i * i;
    let aux2 = aux * i;

    console.log(i, aux, aux2);
    console.log(i, aux+1, aux2+1);

};