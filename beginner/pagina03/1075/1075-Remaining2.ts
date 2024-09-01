const input = `13`;
//const input = require('fs').readFileSync('/dev/stdin', 'utf8');
const lines = +input;

const remaining_2 = (int: number): void => {

    for(let i = 0; i < 10000; i++){
        if(i % int == 2){
            console.log(i)
        }
    }
}

remaining_2(lines)