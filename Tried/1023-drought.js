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

let ints = [];
for (let i = 0; i < lines.length; i++) {
    if (lines[i].length == 1) {
        ints.push(Number(lines[i]))
    }
};

let last = ints[ints.length - 2];

let data = [];
for (let i = 0; i < lines.length; i++) {
    if (lines[i].length !== 1) {
        data.push(lines[i])
    }
};

for (n in ints) {
    if (ints[n] == 0) {
        break

    } else {
        console.log(`Cidade# ${Number(n)+1}:`)
        let aux = []

        for (let i = 0; i < ints[n]; i++) {
            aux.push(data[i].split(' '))
        };

        for (let i = 0; i < ints[n]; i++) {
            data.shift()
        };

        // aux.forEach(item => console.log(item));


        let mediasMoradores = null;
        let exibicaoConsumos = '';

        for (x in aux) {
            let [moradores, consumo] = aux[x];
            let consumoPorMorador = (Number(consumo) / Number(moradores));

            mediasMoradores += consumoPorMorador;

            exibicaoConsumos += `${moradores}-${Math.floor(consumoPorMorador)} `;
        }

        let MediaCidade = Math.round(mediasMoradores / ints[n]);

        console.log(exibicaoConsumos);
        console.log(`consumo medio: ${MediaCidade.toFixed(2)} m3.`);

    }
    
    if(ints[n] !== ints[last]){
        console.log("");
    } 
};