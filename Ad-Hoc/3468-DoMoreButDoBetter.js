console.log(" 3468 - Do more, but do better!");

const input = `INTENSIDADE`;
let lines = input.split('\n');

let test = lines.shift().toLowerCase()

switch(test){

    case 'intensidade':
        console.log('mais');
        break;

    case 'quantidade':
        console.log('mais');
        break;

    default:
        console.log('mas');
        break;
};