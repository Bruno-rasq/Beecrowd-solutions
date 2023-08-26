console.log("1023 - drought");

const input = 
`3
3 22
2 11
3 39
5
1 25
2 20
3 31
2 40
6 70
2
1 1
3 2
0`;

let lines = input.split('\n');

// peguei todos os valores referentes a qnt de casas em cada cidade
let intstg = lines.filter(item => {
    return item.length == 1;
});

let ints = intstg.map(item => Number(item));




console.log(lines);
console.log(ints);









