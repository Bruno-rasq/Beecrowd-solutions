let [ a, b, c ] = lines[0].split(' ');
let arry = [];
arry.push(a, b, c);

let maior = Math.max(...arry);
console.log(`${maior} eh o maior`);