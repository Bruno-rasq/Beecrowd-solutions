const fs = require('fs')
const input = fs.readFileSync('/dev/stdin', 'utf-8')
const [a, b] = input.split(' ').map(Number)

function calcular(x, y){
    let quo = 0

    if((x > 0 && y > 0) || (x < 0 && y > 0)){
        quo = Math.floor(x / y);
    } else {
        quo = Math.ceil(x / y);
    }

    console.log(`${quo} ${x - (y * quo)}`)
}

calcular(a, b)