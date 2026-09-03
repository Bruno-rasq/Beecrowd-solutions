console.log(" 2157 - Mirror Sequence ");

const input = `3
1 5
10 13
98 101`;

let lines = input.split('\n');
let int = Number(lines.shift());
let output = []

for(let i = 0; i < int; i++){

    let data = lines[i].split(' ').map(item => Number(item))
    let line = []

    for(let j = data[0]; j <= data[1]; j++){
        line.push(j)
    }

    let mirror = [...line].join('').split('').reverse().join('')

    output.push(
        `${line.join('')}${mirror}`
    )

}

console.log(output.join('\n'))