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
for ( let i = 0; i< lines.length; i++ ){

    if(lines[i].length == 1){
        loops.push(Number(lines[i]))
    }
    
};

let data = [];
for ( let i = 0; i< lines.length; i++ ){

    if(lines[i].length !== 1){
        data.push(lines[i])
    }
    
};


let resp = []
for ( n in loops){
    for (let i = 0; i<loops[n]; i++){
        resp.push(data[i]) && data.shift()
    }
    resp.sort()
}

resp.forEach(item => console.log(item))

/*
    problemas:
        - preciso remover o item de data que for lido na primeira interação, senão será lido novamente nas proximas
        - como ordenar cada conjunto sem reordenas todos itens no final

*/