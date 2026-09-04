console.log(" 3467 - This is my place ");

const input = `xxL
Lxx`;
let lines = input.split('\n');

function setup(data){
    for(let n = 0; n < data.length - 1; n++){
        let [ x1, x2, x3] = data[n].spnlit('')
        place(x1, x2, x3)
    }
}

function place(n1, n2, n3){
    if(n3 == 'L')
        console.log('Esse eh o meu lugar')

    if( n3 != 'L')
        console.log('Oi, Leonard')
}

setup(lines)