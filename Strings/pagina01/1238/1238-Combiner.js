console.log(" 1238 - Combiner ");

const input = `2
Tpo oCder
aa bb`;

let lines = input.split('\n');
let int = Number(lines.shift());

for(let i = 0; i < int; i++){

    let data = lines[i].split(' ')
    let [ A, B ] = data

    A = A.split('')
    B = B.split('')

    let HighierSize;

    if(A.length > B.length){
        HighierSize = Number(A.length)
    } else {
        HighierSize = Number(B.length)
    }

    let resp = ''

    for(let i = 0; i < HighierSize; i++){
        if(A[i] && B[i]){
            resp += A[i]
            resp += B[i]
        }

        if(!B[i]){
            resp += A[i]
        } 

        if(!A[i]){
            resp += B[i]
        }
    }

    console.log(resp)
};