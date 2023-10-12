console.log(" 1515 - hello galaxy ");

const input = `3
PlanetaXYZ 2014 5
PlanetaDosMacacos 2020 7
JINQEWIOSDFaa 2043 20
2
PlanetaA 2050 10
PlanetaB 2055 16
0`;

let lines = input.split('\n');

function planetResponse(array){

    let planetas = [];
    let anos = [];

    for ( n in array ){
        let data = array[n].split(' ')
        let [ nome, ano, temp ] = data;

        let duracao = Number(ano) - Number(temp)

        planetas.push(nome)
        anos.push(duracao);
    }

    let min = Math.min(...anos);
    return planetas[anos.indexOf(min)];

};

function main(input){

    let output = []

    for(let i = 0; i < input.length; i++){

        let galaxy = []
        let int = Number(input.shift());
        if(int == 0) break

        for(let j = 0; j < int; j++){
            let planet = input.shift()
            galaxy[j] = planet
        }

        let response = planetResponse(galaxy)

        output.push(
            response
        )
    };
    console.log(output.join('\n'))
};

main(lines)