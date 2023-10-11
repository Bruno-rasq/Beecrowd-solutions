console.log(" 3299 - Small Unlucky Numbers ");

const input = `12321`;

let lines = input.trim().split('').map(item => Number(item));

let output = `${lines.join('')} NO es de Mala Suerte`;

for(let i = 0; i < lines.length; i++){
    if(lines[i] == 1 && lines[i+1] == 3){
        output = `${lines.join('')} es de Mala Suerte`
    } 
};

console.log(output)