const fs = require("fs")
const input = fs.readFileSync('/dev/stdin', 'utf8').split("\n");

function fire_flowers(data) {
    const [ r1, x1, y1, r2, x2, y2 ] = data.split(' ').map(Number)
    const distancia_do_centro = Math.sqrt(Math.pow(x2 - x1, 2) + Math.pow(y2 - y1, 2))
    
    distancia_do_centro <= r1 - r2 ? console.log('RICO') : console.log('MORTO')
}

for(let i = 0; i < input.length; i++){
    fire_flowers(input[i])
}