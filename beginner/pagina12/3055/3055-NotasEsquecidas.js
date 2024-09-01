console.log(" 3055 - notas esquecidas ");

const input = `100
70`;

let lines = input.split('\n');
let [ nota1, media ] = lines;

let nota2 = (Number(media) * 2) - nota1;

console.log(nota2);