console.log(" 2453 - lingua do P ");

const input = `pA pppapppa pdpo pPpapppa`;

let lines = input.split(' ');

let resp = [];

for(let i = 0; i<lines.length; i++){
    let data = lines[i].split('');
    let word = removeP(data);
    resp.push(word.join(''))
};

function removeP(arr){

    let aux = [];

    for(let i = 0; i<arr.length; i+=2){
        aux.push(arr[i+1])
    };

    return aux;
};

console.log(resp.join(' ').trim());