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

let lines = input.trim().split('\n');
lines.pop()

let t = 0, p = 0
while(p < lines.length){
    let int = parseInt(lines[p++]);

    if(t){
        console.log('')
    };


    let consumos = Array(201);
    consumos.fill(0);
    let [totalX, totalY] = [0, 0];
    for(let n = 0; n < int; ++n){
        let [X, Y] = lines[p++].split(' ').map(el => Number(el));

        totalX += X;
        totalY += Y;
        consumos[parseInt(Math.floor(Y/X))] += X
    };

    console.log(`Cidade# ${++t}:`);
    let output = []
    for(let i = 0; i < 201; ++i){
        if(consumos[i] > 0) output.push(`${consumos[i]}-${i}`)
    }
    console.log(output.join(' '));

    let consumoTotal = Math.floor(100 * totalY / totalX) / 100;
    console.log(`Consumo medio: ${consumoTotal.toFixed(2)} m3.`)
}



/*

    ERRO: tempo limite excedido;

let lines = input.trim().split('\n');
let output = []

lines.pop();


for(let i = 0, city = 1; i< lines.length; i++, city++){

    let int = Number(lines.shift())

    let consumos = Array(201);
    consumos.fill(0);

    let [totalX, totalY] = [0, 0];
    for(let n = 0; n < int; n++){
        let [X, Y] = lines.shift().split(' ').map(el => Number(el));

        totalX += X;
        totalY += Y;
        consumos[parseInt(Math.floor(Y/X))] += X
    }

    let exibicaoConsumos = []
    for(let j = 0; j < 201; j++){
        if(consumos[j] > 0){
            exibicaoConsumos[j] = `${consumos[j]}-${j}`   
        }
    }

    let exibicao = exibicaoConsumos.filter(el => el != null).join(' ')
    let consumoTotal = Math.floor(100 * totalY / totalX) / 100;

    output.push(
        `Cidade# ${city}:`,
        exibicao,
        `Consumo medio: ${consumoTotal.toFixed(2)} m3.`,
        ''
    );

};

console.log(output.join('\n'))
*/
