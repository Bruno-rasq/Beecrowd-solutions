console.log(" 2457 - letras ");

const input = `j 
jamelao`;

let lines = input.split('\n');

let letter = lines[0].trim().toString();
let words = lines[1].split(' ');

let countWords = Number(words.length);
let count = 0;

for ( n in words ){
    let data = words[n].split('')
    
    if( data.includes(letter) == true ){
        count++
    }
};

let percent = Number((count * 100) / countWords);

console.log(percent.toFixed(1));