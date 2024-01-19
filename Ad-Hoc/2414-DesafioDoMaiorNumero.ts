const input = `99 1000 55 1 2 9 0`;

//const input = require('fs').readFileSync('/dev/stdin', 'utf8');

namespace SETUP {

    export const Set_Data = (data: string): number[] => {
        return data.split(' ').map(element => Number(element))
    }
}

namespace CODE {

    export const Output = (datas: number[]): void => {
        datas.pop()

        console.log(Math.max(...datas))
    }

}

const lines = SETUP.Set_Data(input)
CODE.Output(lines)