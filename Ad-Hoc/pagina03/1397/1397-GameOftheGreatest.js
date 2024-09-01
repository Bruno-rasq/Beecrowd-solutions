console.log(" 1397 - game of the greatest ");

const input = `3
5 3
8 2
5 6
2
3 5
11 10
0`;

let lines = input.split('\n');

while(lines.length){
    let int = Number(lines.shift())

    if(!int) break;

    let [player1, player2] = [0, 0];

    for(let i = 0; i < int; ++i){
        let [A, B] = lines.shift().split(' ').map(el => Number(el))

        if(A > B) player1++
        else if (B > A) player2++
    }

    console.log(`${player1} ${player2}`)
}