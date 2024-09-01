const input = `4
bB
ab
Ee
bAtatA`;

//const input = require('fs').readFileSync('/dev/stdin', 'utf8');

namespace SETUP {

    export const Set_Data = (data: string[]):void => {
        let int = Number(data.shift())
        for(let i = 0; i < int; i++){
            CODE.Output(data[i])
        }
    }
}

namespace CODE {

    const varitions = (str: string): number => {

        let count: number = 1;
        let arr: string[] = Array.from(str, String);
        let chars = ['a', 'e', 'i', 'o', 's']


        for(let n in arr){
            if(chars.includes(arr[n])){
                count *= 3
            } else {
                count *= 2
            }
        }

        return count
        
    }

    export const Output = (password: string): void => {
        console.log(varitions(password.toLowerCase()))
    }

}

SETUP.Set_Data(input.split('\n'))