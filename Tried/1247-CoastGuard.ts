const input = `5 1 12
12 10 7
12 9 10
10 5 5
9 12 15`;

//const input = require('fs').readFileSync('/dev/stdin', "utf8");
const lines = input.split('\n')

// 1 mile == 1609 km

function main(): void {

    while(lines.length){

        let [ D, VF, VG ] = String(lines.shift()).split(' ').map(element => Number(element))

        let tempo_F = 12 / VF;
        let distan_G = Math.sqrt(144 + Math.pow(D, 2))
        let tempo_G = distan_G / VG

        tempo_F < tempo_G ? console.log('N') : console.log('S')

    }
}

main()