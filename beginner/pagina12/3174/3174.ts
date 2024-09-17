const fs = require('fs')
const input = fs.readFileSync('/dev/stdin', 'utf8');
const lines = input.split('\n')
const cases = Number(lines.shift())

let gifts = 0
let restB = 0, restA = 0, restM = 0, restD = 0;

for(let i = 0; i < cases; i++){
    let [name, group, h] = lines[i].split(' ')
    let hours = Number(h)

    if(group == 'bonecos'){
        gifts += Math.floor((hours + restB) / 8)
        restB = (hours + restB) % 8
    }
    if(group == 'arquitetos'){
        gifts += Math.floor((hours + restA) / 4)
        restA = (hours + restA) % 4
    }
    if(group == 'musicos'){
        gifts += Math.floor((hours + restM) / 6)
        restM = (hours + restM) % 6
    }
    if(group == 'desenhistas'){
        gifts += Math.floor((hours + restD) / 12)
        restD = (hours + restD) % 12
    }
}

console.log(gifts)