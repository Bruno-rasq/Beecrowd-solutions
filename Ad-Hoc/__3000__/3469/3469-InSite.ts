const input = `16
1 9 8 6 3 7 5 10 19 20 30 50 13 2 17 4`;

//const input = require('fs').readFileSync('/dev/stdin', 'utf8')
const lines = input.split('\n');


function medianValue(arr: number[], int: number): void {

    if(int <= 0 || int > arr.length) return 

    if(int % 2 != 0){
        console.log(arr[Math.floor(int / 2)])
        return 
    }


    console.log(Math.floor((arr[int / 2] + arr[int / 2 - 1]) / 2))
   
}

function setup(data : string[]): void {

    let int = Number(data.shift())
    
    let arr = data
                .toString()
                .split(' ')
                .map(element => Number(element))
                .sort((a, b) => a - b)

    medianValue(arr, int)
}

setup(lines)