console.log(" 2518 - FNDI's Staircase ");

const input = `4
3 4 30`;

/*

[MINHA RESPOSTA];

    let lines = input.split('\n');
    let d = Number(lines.shift());

    let data = lines[0].split(' ').map(item => parseInt(item));
    let [ h, c, l ] = data

    let areaRampCalc = (Math.hypot(h, c) * d * l) * 1e-4;

    console.log(areaRampCalc.toFixed(4));

*/

let lines = input.split('\n').map((line) => line.split(" ", 3)
.map((value) => Number.parseInt(value, 10)));

let calcRampArea = (d, h, c, l) => (Math.hypot(h, c) * d * l) * 1e-4;

const output = []

for (let i = 0; i < lines.length; i += 2) {
    const [N] = lines[i + 0]

    if (isNaN(N)) break // EOF

    const [H, C, L] = lines[i + 1]
    const area = calcRampArea(N, H, C, L)

    output.push(area.toFixed(4))
}

console.log(output.join("\n"));