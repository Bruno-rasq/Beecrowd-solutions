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

// percorre todos as lines separandos os dados de moradores/consumo
for(let i = 0; i < int; i++){

    let data = lines[i].split(/\s+/);
    let [ moradores, consumo ] = data;

    // gera uma media de consumo para cada casa
    let consumoPorMorador = (Number(consumo) / Number(moradores));

    mediasMoradores += consumoPorMorador;

}

// guarda a media de consumo por cidade
let MediaCidade = Math.round(mediasMoradores / int);

console.log(`consumo medio: ${MediaCidade.toFixed(2)} m3`);