console.log(" 1515 - hello galaxy ");

const input = `3
PlanetaN 2111 02
PlanetaD 2100 10
PlanetaJ 1000 01
3
Planetinha 2010 01
PlanetaC 2000 10
Planetoide 2100 30
0`;

let lines = input.split('\n');

let ints = [];
let data = [];

for (let i = 0; i < lines.length; i++) {
    if (lines[i].length == 1) {
        ints.push(Number(lines[i]))

    } else if (lines[i].length !== 1) {
        data.push(lines[i])
    } 
};


for(n in ints){
    if(ints[n] == 0){
        break;

    } else {

        let aux = [];

        for ( let i = 0; i<ints[n]; i++ ){
            aux.push(data[i])
        }
        for ( let i = 0; i<ints[n]; i++ ){
            data.shift()
        }

        let resp = planet(aux);
        console.log(resp)

    }
}

function planet(array){

    let planetas = [];
    let anos = [];

    for ( n in array ){
        let data = array[n].split(' ')

        let [ nome, ano, temp ] = data;
        ano = Number(ano)
        temp = Number(temp)

        let duracao = ano - temp

        planetas.push(nome)
        anos.push(duracao);
    }

    let min = Math.min(...anos);
    return planetas[anos.indexOf(min)];

};