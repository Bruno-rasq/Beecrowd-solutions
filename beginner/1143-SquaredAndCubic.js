console.log(" 1143 - squared and cubic");

const input = `5`;
let lines = input.split('\n');
let int = Number(lines[0]);

for ( let i = 1; i<int+1; i++ ){

    let squal = Math.pow(i, 2);
    let cubic = Math.pow(i, 3);

    console.log( i, squal, cubic );
};