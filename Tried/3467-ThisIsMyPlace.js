console.log(" 3467 - This is my place ");

const input = `xxL
Lxx`;
let lines = input.split('\n');

lines.forEach( el => {
    if(el === 'xxL' || el === 'xxl') console.log(`Esse eh o meu lugar`)
    else console.log(`Oi, Leonard`)
})