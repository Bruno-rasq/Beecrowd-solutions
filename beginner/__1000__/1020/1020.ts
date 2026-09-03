const fs = require('fs')
const input = fs.readFileSync('/dev/stdin', 'utf-8')
const num = Number(input)

function ageTodays(n) {

    let age = Math.floor(n / 365);
    let rest = (n - (365 * age));

    let month = Math.floor(rest / 30);
    let days = (rest - (30 * month));

    console.log(`${age} ano(s)`);
    console.log(`${month} mes(es)`);
    console.log(`${days} dia(s)`);

}

ageTodays(num);