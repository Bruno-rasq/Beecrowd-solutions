console.log(" 3048 - sequencia secreta ");

const input = `12
1
2
1
2
2
2
1
1
2
2
1
1`;

let lines = input.split('\n');
let int = Number(lines.shift());

let count = 0;
let aux = 0;

for (let i = 0; i< int; i++){

    let current = Number(lines[i])

    if(current != aux){
        count++
    }
    
    aux = current;
};

console.log(count);