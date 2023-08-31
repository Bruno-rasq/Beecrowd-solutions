console.log(" 2936 - how much cassava? ");

const input = `5
4
3
2
1`;

let lines = input.split('\n');
let porcoes = [300, 1500, 600, 1000, 150];

let response = null;

for(let i = 0; i< lines.length; i++){

    response += Number(lines[i]) * porcoes[i];

};

response += 225

console.log(typeof response);
console.log(response);


/*
    o código dá as respostas certas para todos os casos porem não passa no teste
    apresentando 100% de erro

    typeOf diz que é um number porem o teste diz que é NaN. 

*/