console.log(" 3469 - In site");

const input = `13
1 9.5 6 3 7 5 10 20 30 50 13 2 17`;
let lines = input.split('\n');

function medianValue(arr, int) {

    if(int <= 0 || int > arr.length) return 

    if(int % 2 != 0){
        console.log(arr[Math.floor(int / 2)])
        return 
    }

    console.log(Math.floor((arr[int / 2] + arr[int / 2 - 1]) / 2))
   
}

function setup(data) {

    let int = Number(data.shift())
    
    let arr = data
                .toString()
                .split(' ')
                .map(element => Number(element))
                .sort((a, b) => a - b)

    medianValue(arr, int)
}

setup(lines)