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

    let simplify = "";

    switch (currentData[3]) {

        case '+':
            nom = ((n1 * d2) + (n2 * d1));
            den = (d1 * d2);

            response = `${nom}/${den}`;

            for(let i = Math.max(nom, den); i > 1; i--){
                if ((nom % i == 0) && (den % i == 0)) {
                    nom /= i;
                    den /= i;
                }
            }

            if(den === 1){
                simplify = `${nom}`;
            } else {
                simplify = `${nom}/${den}`;
            }

            console.log(`${response} = ${simplify}`);
            break;

        case '-':
            nom = ((n1 * d2) - (n2 * d1));
            den = (d1 * d2);

            response = `${nom}/${den}`;

            for(let i = Math.max(nom, den); i > 1; i--){
                if ((nom % i == 0) && (den % i == 0)) {
                    nom /= i;
                    den /= i;
                }
            }

            if(den === 1){
                simplify = `${nom}`;
            } else {
                simplify = `${nom}/${den}`;
            }

            console.log(`${response} = ${simplify}`);
            
            break;

        case '*':
            nom = (n1 * n2);
            den = (d1 * d2);

            response = `${nom}/${den}`;

            for(let i = Math.max(nom, den); i > 1; i--){
                if ((nom % i == 0) && (den % i == 0)) {
                    nom /= i;
                    den /= i;
                }
            }

            if(den === 1){
                simplify = `${nom}`;
            } else {
                simplify = `${nom}/${den}`;
            }

            console.log(`${response} = ${simplify}`);
            break;

        case '/':
            nom = (n1 * d2);
            den = (n2 * d1);

            response = `${nom}/${den}`;

            for(let i = Math.max(nom, den); i > 1; i--){
                if ((nom % i == 0) && (den % i == 0)) {
                    nom /= i;
                    den /= i;
                }
            }

            if(den === 1){
                simplify = `${nom}`;
            } else {
                simplify = `${nom}/${den}`;
            }

            console.log(`${response} = ${simplify}`);
            break;

        default:
    };
};
