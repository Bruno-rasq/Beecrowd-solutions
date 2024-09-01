console.log(" 2339 - avioes de papel ");

const input = `10 90 10`;

let lines = input.split(' ');
let [alunos, folhas, chances] = lines;

if(Number(alunos) * Number(chances) <= Number(folhas)){
    console.log('s');
} else {
    console.log('n')
}