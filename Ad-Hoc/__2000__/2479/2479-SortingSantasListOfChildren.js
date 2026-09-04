console.log(" 2479 - Sorting Santa's List of Children ");

const input = `16
+ Tininha
+ Dudinha
- Carlinhos
- Marquinhos
+ Joaozinho
+ Bruninha
- Leandrinho
- Fernandinha
+ Rafinha
- Pedrinho
+ Aninha
- Tamirinha
- Gaguinho
- Zezinho
- Luquinhas
+ Julhinha`;

let lines = input.split('\n');
let int = Number(lines.shift());
let output = []
let names = []
let bons = 0
let maus = 0

for(let i = 0; i < int; i++){
    let data = lines[i].split(' ');

    names.push(data[1])

    if(data[0] == '+'){
        bons++
    }

    if(data[0] == '-'){
        maus++
    }
}

output.push(
    names.sort((a, b) => a.localeCompare(b)).join('\n'),
    `Se comportaram: ${bons} | Nao se comportaram: ${maus}`
)

console.log(output.join('\n'))