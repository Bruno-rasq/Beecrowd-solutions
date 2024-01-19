const input = `6 7
2 1 3 4 0 6 5
5 4
5 3 0 1
5 3
1 5 0
0 0`;

//const input = require('fs').readFileSync('/dev/stdin', 'utf8');
const lines = input.split('\n').filter(line => line !== '0 0');

namespace SETUP {

    export const Set_Data = (data: string): number[] => {
        return data.split(' ').map(element => Number(element))
    }
}

namespace CODE {

    const bingo = (N: number, B: number, balls: number[]) => {

        let set_balls = new Set();
        set_balls.add(0)

        for(let i = 0; i < B; i++){
            for(let j = i + 1; j < B; j++){
                set_balls.add(Math.abs(balls[i] - balls[j]))
            }
        }

        return set_balls.size === N + 1 ? 'Y' : 'N'
    }


    export const Output = (datas: string[]): void => {

        while(datas.length){

            let [N, B] = SETUP.Set_Data(String(datas.shift()))
            let Balls = SETUP.Set_Data(String(datas.shift()))

            console.log(bingo(N, B, Balls))
        }
    }

}

CODE.Output(lines)