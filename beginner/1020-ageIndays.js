/*
    Read an integer value corresponding to a person's age (in days) and print it in years, months and days, followed by its respective message “ano(s)”, “mes(es)”, “dia(s)”.

    Note: only to facilitate the calculation, consider the whole year with 365 days and 30 days every month. In the cases of test there will never be a situation that allows 12 months and some days, like 360, 363 or 364. This is just an exercise for the purpose of testing simple mathematical reasoning.

    Input
    The input file contains 1 integer value.

    Output
    Print the output, like the following example.

*/

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
