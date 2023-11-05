console.log(" 1278 - Justifier II ");

const input = `3
ROMEO      AND
 JULIET WERE  
   IN LOVE    
4
WHO
ELSE
LOVES
STAIRS
3
A TEXT CAN BE JUSTIFIED
ON   BOTH   SIDES    OR
JUST   TO   THE   RIGHT
0`;

let lines = input.split('\n')

let first = true
while(lines.length){
    let int = Number(lines.shift())
    if(!int) break

    if(first)   first = false;
    else        console.log('');

    let aux = []
    for(let j = 0; j < int; j++){
        aux.push(lines.shift().trim().replace(/\s+/g, ' '))
    }

    let Max = aux.reduce((acc, cur) => acc < cur.length ? cur.length : acc, 0);
    
    for(let n = 0; n < int; n++){
        console.log(aux[n].padStart(Max))
    }
}