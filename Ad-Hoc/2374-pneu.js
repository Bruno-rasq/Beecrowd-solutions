console.log(" 2374 - pneu ");


const input = `30
18`;

let lines = input.trim().split('\n');
let [ n1, n2 ] = lines;
n1 = Number(n1);
n2 = Number(n2);

let response = null;

if(n1 > n2){
    response = (n1 - n2);
} else if ( n1 < n2){
    response = - (n2 - n1);
} else {
    response = 0;
};

console.log(response);