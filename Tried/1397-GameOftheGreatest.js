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

function main() {

    for (let i = 0; i < lines.length; i++) {

        let rounds = Number(lines.shift());
        if (rounds == 0) break;

        let count_player1 = 0;
        let count_player2 = 0;

        for (let j = 0; j < rounds; j++) {
            let math = lines.shift().split(' ').map(item => Number(item));
            let [player1, player2] = math;

            if (player1 < 0 || player1 > 10 || player2 < 0 || player2 > 10){
                 break
                
            } else {

                if (player1 > player2) {
                    count_player1++
                } else if (player1 < player2) {
                    count_player2++
                } else {
                    break
                };
            }
        };

        console.log(`${count_player1} ${count_player2}`);
    };

};

main()