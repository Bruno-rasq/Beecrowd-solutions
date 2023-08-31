console.log(" 1157 - divisors 1 ");

const input = `6`;
let lines = input.split('\n');

let N = Number(lines[0]);

for(let i = 0; i <= N; i++){

    if(N%i == 0){
        console.log(i)
    }
};