console.log("1023 - drought");

const input = `3
3 22
2 11
3 39`;

let lines = input.split('\n');
let int = Number(lines.shift());

console.log(int);



// guarda as medias de consumo por residencia
let mediasMoradores = null;

let exibicaoConsumos = '';

// percorre todos as lines separandos os dados de moradores/consumo
for(let i = 0; i < int; i++){

    let data = lines[i].split(/\s+/);
    let [ moradores, consumo ] = data;

    // gera uma media de consumo para cada casa
    let consumoPorMorador = (Number(consumo) / Number(moradores));

    mediasMoradores += consumoPorMorador;

    exibicaoConsumos += `${moradores}-${Math.floor(consumoPorMorador)} `;

}

// guarda a media de consumo por cidade
let MediaCidade = Math.round(mediasMoradores / int);

console.log(exibicaoConsumos);
console.log(`consumo medio: ${MediaCidade.toFixed(2)} m3`);









// const input = 
// [`3
// 3 22
// 2 11
// 3 39`,

// `5
// 1 25
// 2 20
// 3 31
// 2 40
// 6 70`,

// `2
// 1 1
// 3 2`,

// `0`];

// let lines = input.map(item => item.split('\n'));

// // guarda os valores int, serve de loop para as cidades
// let int = [];

// for(let i = 0; i < lines.length; i++){

//     int.push(Number(lines[i].shift()));

// };

// console.log(int);