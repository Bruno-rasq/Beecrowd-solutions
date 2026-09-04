console.log(" 2375 - sedex ");

const input = `3
2 3 5`;

let lines = input.split('\n');

let diametro = Number(lines[0]);
let [altura, largura, profundidade] = lines[1].split(' ').map(item => Number(item))
let output = diametro <= Math.min(altura, largura, profundidade)
 
console.log(output ? 'S' : 'N')