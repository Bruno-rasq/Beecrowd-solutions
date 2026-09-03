console.log(" 1120 - Contract Revision");

const input = `5 5000000
3 123456
9 23454324543423
9 99999999991999999
7 777
0 0`;

let lines = input.split('\n');

while(lines.length){
    let [D, N] = lines.shift().trim().split(' ');

    if(D === '0' && N === '0') break;

    N = N.split('').filter(x => x != D).join('')

    let regex = /^(0+)/i;
    let response = N.match(regex);

    if(response) N = N.replace(response[0], '')

    if(N.length === 0){
        console.log('0')
    }
    else {
        console.log(N)
    }
}