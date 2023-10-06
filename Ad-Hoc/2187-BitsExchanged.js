console.log(" 2187 - Bits Exchanged ");

const input = `1
72
0`;

let lines = input.split('\n').map(i => Number(i));

let response = []

for(let i = 0; i < lines.length; i++){

    if(lines[i] == 0) break

    let valor = lines[i]

    let cin = (Math.floor( valor / 50 )).toFixed(0);
    let restCin = valor % 50;

    let dez = (Math.floor( restCin  / 10 )).toFixed(0);
    let restDez = valor % 10;

    let cinc = (Math.floor( restDez / 5 )).toFixed(0);
    let restCinc = valor % 5;

    let um = (Math.floor( restCinc / 1 )).toFixed(0);
    
    let notes = [cin, dez, cinc, um]

    response.push(
        `Teste ${i+1}`,
        notes.join(' '),
        ''
    )
}

console.log(response.join('\n'));