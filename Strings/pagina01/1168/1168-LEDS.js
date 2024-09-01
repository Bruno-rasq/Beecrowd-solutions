console.log(" 1168 - LED ");

const input = `3
115380
2819311
23456`;

let lines = input.trim().split('\n');
let int = Number(lines.shift());


for (let i = 0; i < int; i++){

    let data = lines[i].split('')
    let response = Count(data)
    console.log(`${response} leds`)

};

function Count(arr){

    let leds = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6];
    let count = 0

    for( n in arr ){
        count += leds[ Number(arr[n]) ]
    }

    return count
};