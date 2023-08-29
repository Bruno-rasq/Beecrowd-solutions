console.log(" 1985 - macPronalts ");

const input = `2
1001 2
1005 3`;

let lines = input.split('\n');
let int = Number(lines.shift());

let response = null;

for (let i = 0; i < int; i++) {

    let data = lines[i].split(' ');
    let [ code, qnt ] = data;

    let price = null;

    switch(code){
        case '1001':
            price = 1.50;
            break;

        case '1002':
            price = 2.50;
            break;

        case '1003':
            price = 3.50;
            break;

        case '1004':
            price = 4.50;
            break;

        case '1005':
            price = 5.50;
            break;

        default:
    };

    response += price * Number(qnt);

}

console.log(response.toFixed(2));