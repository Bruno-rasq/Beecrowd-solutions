function ageTodays(n) {

    let age = Math.floor(n / 365);
    let rest = (n - (365 * age));

    let month = Math.floor(rest / 30);
    let days = (rest - (30 * month));

    console.log(age, month, days)
}

ageTodays(400);
ageTodays(800);
ageTodays(30);



let n = Number(lines[0]);

let age = Math.floor(n / 365);
let rest = (n - (365 * age));

let month = Math.floor(rest / 30);
let days = (rest - (30 * month));

console.log(`${age} ano(s)`);
console.log(`${month} mes(es)`);
console.log(`${days} dia(s)`);
