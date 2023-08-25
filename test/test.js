console.log("1023 - drought");

const input = `3
3 22
2 11
3 39`;

let lines = input.split('\n');
let int = Number(lines.shift());

console.log(int);

for(let i = 0; i < int; i++){

    let data = lines[i].split(/\s+/);
    let [ moradores, consumo] = data;


    console.log(data, Number(moradores), Number(consumo));
}

