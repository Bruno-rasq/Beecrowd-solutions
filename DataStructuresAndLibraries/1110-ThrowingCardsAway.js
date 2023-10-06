console.log(" 1110 - Throwing Cards Away ");

const input = `7
19
10
6
0`;

let lines = input.split('\n');
let output = []


for(let i = 0; i < lines.length; i++){

    let cardsNumber = Number(lines[i]);

    if(cardsNumber == 0) break;

    let cards = []
    let count = 1
    for(let n = 0; n < cardsNumber; n++){
        cards.push(
            count++,
        )
    }

    let resp = response(cards)
    let rest = resp.pop();

    output.push(
        `Discarded cards: ${resp.join(', ')}`,
        `Remaining card: ${rest}`
    )
}

function response(arry){

    let discarted = []
    let size = arry.length;

    for(let i = 0; i < size; i++){
        let disc = arry.shift()
        let aux = arry.shift()

        discarted.push(
            disc
        )

        arry.push(aux)
    }

    return discarted
}


console.log(output.join('\n'))