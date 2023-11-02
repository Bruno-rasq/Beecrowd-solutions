console.log(" 3469 - In site");

const input = `13
1 9.5 6 3 7 5 10 20 30 50 13 2 17`;
let lines = input.split('\n');

function Quicksort(arr){

    if(arr.length < 2){
        return arr
    }

    let pivo = arr[arr.length - 1];
    let left = [];
    let right = [];
    for(let i = 0; i < arr.length - 1; i++){
        if(arr[i] < pivo){
            left.push(arr[i])
        } else {
            right.push(arr[i])
        }
    }

    return [...Quicksort(left), pivo, ...Quicksort(right)]
};

function main(input){

    let int = Number(input.shift());
    let array = input.shift().split(' ').map(i => Number(i))
    let sortedArr = Quicksort(array);

    let pivo = Math.floor((sortedArr.length) / 2)
    let even = Number(sortedArr[pivo]) + Number(sortedArr[pivo - 1]);
    let odd = Number(sortedArr[pivo])

    let response = int % 2 == 0 ? parseInt(even) : parseInt(odd);
    console.log(response)

};

main(lines);