console.log(" 2189 - Kermesse ");

const input = `4
4 5 3 1
10
9 8 7 6 1 4 3 2 12 10
0`;

let lines = input.trim().split("\n");
let output = []

for(let i = 0; i < lines.length; i++){

    let int = Number(lines.shift())
    let arr = lines.shift().split(' ').map(i => Number(i));

    if(int === 0) break; // end line

    for(let j = 0; j < int; j++){
        if(arr[j] === j + 1){
            output.push(
                `Teste ${i+1}`,
                arr[j],
                ''
            )
        }
    }
}

console.log(output.join('\n'))