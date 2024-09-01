console.log(" 2958 - The bad vibes walk");

const input = `3 3
7V 1D 2D
2D 1V 1V
3V 5V 9D`

let lines = input.split('\n');
let [lin, col] = lines.shift().split(' ');
lin = Number(lin);
col = Number(col);

let lineTotal = [];

for (let i = 0; i < lin; i++) {
    
    let row = lines[i].split(' ').sort();

    for (let n = 0; n < col; n++){
        let col = row[n].split(' ');

        lineTotal.push(col.toString())
    }
}

let response = [];


let V = lineTotal.filter(char => {
    return char.includes('V')
});
V.sort().reverse()

let D = lineTotal.filter(char => {
    return char.includes('D')
});

D.sort().reverse();

for (n in V){
    response.push(V[n])
};

for (n in D){
    response.push(D[n])
};

for ( n in response ){
    console.log(response[n])
};
