import * as fs from "fs"

const input = fs.readFileSync('/dev/stdin', 'utf8');
const lines = input.trim().split('\n');

function fire_flowers(data: string): void {
    const [ r1, x1, y1, r2, x2, y2 ] = data.split(' ').map(el => Number(el))

    const distancia_do_centro = Math.sqrt(Math.pow(x2 - x1, 2) + Math.pow(y2 - y1, 2))
    distancia_do_centro <= r1 - r2 ? console.log('RICO') : console.log('MORTO')
}

lines.forEach(line => {
    fire_flowers(line)
})