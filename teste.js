
function ageTodays(n){

    let age = Math.floor(n / 365);
    let rest = (n - (365 * age));

    let month = Math.floor(rest / 30);
    let days = (rest - (30 * month));

    console.log(age, month, days)
}

ageTodays(400);
ageTodays(800);
ageTodays(30);