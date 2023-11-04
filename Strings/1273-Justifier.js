console.log(" 1273 - Justifier ");

const input = `3
BOB
TOMMY
JIM
4
JOHN
JAKE
ALAN
BLUE
4
LONGEST
A
LONGER
SHORT
0`;

let lines = input.split('\n');

let first = true
while(lines.length){
    let int = Number(lines.shift())
    if(!int) break

    if(first)   first = false;
    else        console.log('');

    let aux = []
    for(let j = 0; j < int; j++){
        aux.push(lines.shift().trim())
    }

    let Max = aux.reduce((acc, cur) => acc < cur.length ? cur.length : acc, 0);
    
    for(let n = 0; n < int; n++){
        console.log(aux[n].padStart(Max))
    }
}