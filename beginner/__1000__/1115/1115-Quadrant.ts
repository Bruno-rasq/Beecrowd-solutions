const input = `2 2
3 -2
-8 -1
-7 1
0 2`;

//const input = require('fs').readFileSync('/dev/stdin', 'utf8');
const lines = input.split('\n');

namespace SETUP {

    export const Set_Data = (data: string): number[] => {
        return data.split(' ').map(element => Number(element))
    }
}

namespace CODE {

    export const quadrant = (x: number, y: number): string => {
        let response = '';

        if(x > 0 && y > 0) response = 'primeiro'
        if(x < 0 && y > 0) response = 'segundo'
        if(x < 0 && y < 0) response = 'terceiro'
        if(x > 0 && y < 0) response = 'quarto'

        return response
    }

    export const Output = (datas: string[]): void => {

        for(let i = 0;  i< datas.length; i++){

            let [ x, y ] = SETUP.Set_Data(datas[i])

            if(x == 0 || y == 0) break

            console.log(quadrant(x, y))
        }
    }

}

CODE.Output(lines)