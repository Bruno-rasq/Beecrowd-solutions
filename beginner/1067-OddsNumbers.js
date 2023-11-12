console.log(" 1067 - Odd Numbers ");

const input = `9`;
let lines = input.split('\n');

let int = Number(lines.shift());
let odds = []

let T = 1;
while(T <= int){

    if(T % 2 != 0){
        odds.push(T)
    }

    T++
};

odds.forEach(el => console.log(el))