console.log(" 1022 - TDA rational ");

let input = `4
1 / 2 + 3 / 4
1 / 2 - 3 / 4
2 / 3 * 6 / 6
1 / 2 / 3 / 4`;

let lines = input.split('\n');

let int = Number(lines.shift());


for (let i = 0; i < int; i++) {

    let currentData = lines[i].split(/\s+/);

    let n1 = parseInt(currentData[0]);
    let d1 = parseInt(currentData[2]);
    let n2 = parseInt(currentData[4]);
    let d2 = parseInt(currentData[6]);

    let nom = null;
    let den = null;
    let simp = null;

    switch (currentData[3]) {

        case '+':
            nom = ((n1 * d2) + (n2 * d1));
            den = (d1 * d2);

            simp = simplifyFrac(nom, den);

            console.log(`${nom}/${den} = ${simp}`);
            break;

        case '-':
            nom = ((n1 * d2) - (n2 * d1));
            den = (d1 * d2);

            simp = simplifyFrac(nom, den);

            console.log(`${nom}/${den} = ${simp}`);
            
            break;

        case '*':
            nom = (n1 * n2);
            den = (d1 * d2);

            simp = simplifyFrac(nom, den);

            console.log(`${nom}/${den} = ${simp}`);
            break;

        case '/':
            nom = (n1 * d2);
            den = (n2 * d1);

            simp = simplifyFrac(nom, den);

            console.log(`${nom}/${den} = ${simp}`);
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

    if(d == 1){
        simplify = `${n}/1`;
    } else {
        simplify = `${n}/${d}`;
    }

    return simplify;
};



