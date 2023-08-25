
console.log(" 1022 - TDA rational ");

let input = `4
1 / 2 + 3 / 4
1 / 2 - 3 / 4
2 / 3 * 6 / 6
1 / 2 / 3 / 4`;

let lines = input.split('\n');

let int = Number(lines.shift());


for (let i = 0; i < int; i++) {

    let currentData = lines[i].split(/\s+/).join('');

    let n1 = Number(currentData[0]);
    let d1 = Number(currentData[2]);
    let n2 = Number(currentData[4]);
    let d2 = Number(currentData[6]);

    let response = "";
    let nom = null;
    let den = null;
    let simp = null;

    switch (currentData[3]) {

        case '+':
            nom = ((n1 * d2) + (n2 * d1));
            den = (d1 * d2);

            response = `${nom}/${den}`;
            simp = simplifyFrac(nom, den);

            console.log(`${response} = ${simp}`);
            break;

        case '-':
            nom = ((n1 * d2) - (n2 * d1));
            den = (d1 * d2);

            response = `${nom}/${den}`;
            simp = simplifyFrac(nom, den);

            console.log(`${response} = ${simp}`);
            
            break;

        case '*':
            nom = (n1 * n2);
            den = (d1 * d2);

            response = `${nom}/${den}`;
            simp = simplifyFrac(nom, den);

            console.log(`${response} = ${simp}`);
            break;

        case '/':
            nom = Number(n1 * d2);
            den = Number(n2 * d1);

            response = `${nom}/${den}`;
            simp = simplifyFrac(nom, den);

            console.log(`${response} = ${simp}`);
            break;

        default:
    };
};

function simplifyFrac(n, d){

    let simplify = "";

    for(let i = Math.max(n, d); i > 1; i--){
        if ((n % i == 0) && (d % i == 0)) {
            n /= i;
            d /= i;
        }
    }

    if(d === 1){
        simplify = `${n}`;
    } else {
        simplify = `${n}/${d}`;
    }

    return simplify;
};


/*
    OBS: 
        o código não passa no teste pois o beecrowd está reclamando o resultado como NaN
        sendo que toda vez que for concatenar uma variável Number com uma string a mesma 
        se torna string tbm.

        não sei como resolver esta problematica

*/