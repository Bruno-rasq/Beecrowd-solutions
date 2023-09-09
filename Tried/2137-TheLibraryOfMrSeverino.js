console.log(" 2137 - The Library of Mr. Severino ");

const input = `3
1233
0015
0100
7
0752
1110
0001
6322
8000
6321
0000`;

let lines = input.split('\n');

let loops = [];
for ( let i = 0; i<lines.length; i++ ){

    if(lines[i].length == 1){
        loops.push(Number(lines[i]))
    }
    
};

let data = [];
for ( let i = 0; i<lines.length; i++ ){

    if(lines[i].length !== 1){
        data.push(lines[i])
    }
    
};


let resp = []

for ( n in loops){
    
    let aux = []

    for(let i = 0; i < loops[n]; i++){
        aux.push(data[i])
    };

    for(let i = 0; i < loops[n]; i++){
        data.shift()
    };

    aux.sort();
    resp.push(aux);
    aux = [];
}

resp.forEach(item => {
    item.forEach(i => console.log(i))
});