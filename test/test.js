console.log(" 2453 - lingua do P ");

const input = `pA pppapppa pdpo pPpapppa`;

let lines = input.split('\n');

let resp = '';

for (n in lines) {
    let data = lines[n].split('')

    let A = data.filter(char => {
        return char !== 'p'
    });

    resp += `${A.join('')} `

}

console.log(resp)
