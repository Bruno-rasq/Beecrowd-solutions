console.log(" 1171 - Number Frequence ");

const input = `7
8
10
8
260
4
10
10`;

let lines = input.trim().split("\n").map(i => Number(i));
let int = Number(lines.shift());
let output = []

function sort(arr){

    if(arr.length < 2){
        return arr
    }

    let pivo = arr[arr.length - 1];
    let left = []
    let right = []

    for(let i = 0; i < arr.length - 1; i++){
        if(arr[i] < pivo){
            left.push(arr[i])
        } else {
            right.push(arr[i])
        }
    }

    return [...sort(left), pivo, ...sort(right)]
}

let sortedArr = sort(lines)

for(let i = 0; i < int; i++){
    let count = 1;
    let current = sortedArr[i]

    while(i < int && sortedArr[i] === sortedArr[i+1]){
        count++
        i++
    }

    output.push(`${current} aparece ${count} vez(es)`)
}

console.log(output.join('\n'))