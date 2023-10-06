console.log("1023 - drought");

const input = `3
3 22
2 11
3 39
5
1 25
2 20
3 31
2 40
6 70
2
1 1
3 2
0`;

let lines = input.split('\n');

let output = []

for(let i = 0, city = 1; i< lines.length; i++, city++){

    let int = Number(lines.shift())
    if( int == 0 || int == '') break;


    let mediasMoradores = null;
    let exibicaoConsumos = [];

    for(let n = 0; n < int; n++){
        let [ moradores, consumo ] = lines.shift().split(' ').map(el => Number(el))
        let consumoPorMorador = Number(consumo / moradores);

        mediasMoradores += consumoPorMorador;

        exibicaoConsumos[n] = `${moradores}-${Math.floor(consumoPorMorador)}`;
    }

    let MediaCidade = (mediasMoradores / int).toFixed(2);

    output.push(
        `Cidade# ${city}:`,
        exibicaoConsumos.join(' '),
        `Consumo medio: ${MediaCidade} m3.`,
        ''
    )
};

console.log(output.join('\n'))