const input = `6 -8 2 3 0 0
7 3 4 2 4 5
3 0 0 4 0 0
5 4 7 1 8 7`

const lines = input.split('\n')

//const input = require('fs').readFileSync('/dev/stdin', 'utf8');
//const lines = input.trim().split('\n');

lines.forEach(line => {
    fire_flowers(line)
})

function fire_flowers(data: string): void {
    const [ r1, x1, y1, r2, x2, y2 ] = data.split(' ').map(el => Number(el))

    const distancia_do_centro = Math.sqrt(Math.pow(x2 - x1, 2) + Math.pow(y2 - y1, 2))
    distancia_do_centro <= r1 - r2 ? console.log('RICO') : console.log('MORTO')
}

// input line: R1 (1 ≤ R1) , X1(|X1|), Y1(|Y1|), R2 (R2 ≤ 1000), X2(|X2|), Y2 (Y2 ≤ 1000 ).
// r1 raio circulo 1 -- r2 raio circulo 2