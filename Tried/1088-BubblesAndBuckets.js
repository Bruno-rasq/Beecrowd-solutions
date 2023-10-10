console.log(" 1088 - Bubbles and Buckets ");

const input = `5 1 5 3 4 2
5 5 1 3 4 2
5 1 2 3 4 5
6 3 5 2 1 4 6
5 5 4 3 2 1
6 6 5 4 3 2 1
0`;

let lines = input.split('\n');
let output = []

for(let i = 0; i < lines.length; i++){

    let data = lines[i].split(' ').map(item => Number(item));
    if(data[0] == 0) break; // ignora Caso 0

    // bubble sort
    let temp;
    for(let j = 0; j < data.length; j++){
        for(let n = 0; n < data.length - (j - 1); n++){
            if(data[n] > data[n+1]){
                temp = data[n+1]
                data[n+1] = data[n]
                data[n] = temp
            }
        }
    };

    output.push(
        data.join(' ')
    )
}

console.log(output.join('\n'))