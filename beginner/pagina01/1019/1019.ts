const fs = require("fs")
const input = fs.readFileSync('/dev/stdin', 'utf-8')
const num = Number(input)

function TimeConvert(n) {

    let hours = Math.floor(n / 3600);
    let minu = Math.floor((n - (hours * 3600)) / 60);
    let second = Math.floor(n % 60);

    console.log(`${hours.toFixed(0)}:${minu.toFixed(0)}:${second}`);

}

TimeConvert(num);