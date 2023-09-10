console.log(" 2453 - lingua do P ");

const input = `po pppipnptpipnphpo pfpapz pppipu pppipu pa pgpaplpipnphpa pfpapz pppo pppo pe po ppprpopgprpapmpapdpopr pfpapz pppopdpe pppo pcpapfpe`;

let lines = input.split(' ');

let resp = '';

for(let i = 0; i<lines.length; i++){
    let data = lines[i].split('');
    let word = removeP(data);
    resp += `${word.join('')} `;
};

function removeP(arr){
    let aux = [];
    for(let i = 0; i<arr.length; i+=2){
        aux.push(arr[i+1])
    };
    return aux;
};

console.log(resp);

/*
    começando a me frustrar com os desafios errados desse site:

    OBS: o código está correto, traduz a lingua do P normalmente  sem nenhum problema
    e mesmo assim continua a dar erro. no beecrowd tem muitas questões aonde não é possivel 
    chegar em uma resposta correta alem de não ter um suport 

*/