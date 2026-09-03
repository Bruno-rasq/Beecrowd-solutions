const fs = require('fs')
const input = fs.readFileSync('/dev/stdin', 'utf8');
const lines = input.split('\n')

while(lines.length){
    let [ah, am] = lines.shift().trim().split(" ").map(Number)
    let hora = Math.floor(ah / 30).toString().padStart(2, "0");
    let minuto = Math.floor(am / 30).toString().padStart(2, "0");

    console.log(`${hora}:${minuto}`)
}