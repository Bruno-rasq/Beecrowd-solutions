const input = `200
100`;

//const input = require('fs').readFileSync('/dev/stdin', 'utf8')
const lines = input.split('\n').map(element => Number(element));


const HIGH_And_POSITION = (data : number[]): void  => {

    let max: number = 0
    let pos: number = 0

    for(let i = 0; i < 100; i++){
        if(data[i] > max){
            max = data[i]
            pos = i + 1
        }
    }

    console.log(max)
    console.log(pos)
}

HIGH_And_POSITION(lines)