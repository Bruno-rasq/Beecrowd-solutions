const input = `14 40 12 60`

//const input = require('fs').readFileSync("/dev/stdin", "utf8");
const lines = input.split(' ').map(element => Number(element));

function istriangle (a: number, b: number, c: number) : boolean {

    let cond1 = Math.abs(a - b) < c;
    let cond2 = Math.abs(b - c) < a;
    let cond3 = Math.abs(a - c) < b;
    let cond4 = a < b + c;
    let cond5 = b < a + c;
    let cond6 = c < a + b;

    return cond1 && cond2 && cond3 && cond4 && cond5 && cond6
}

function main(): void {

    let [ a, b, c, d ] = lines

    let response = istriangle(a, b, c) 
    || istriangle(b, c, d) 
    || istriangle(a, c, d) 
    || istriangle(b, a, d)

    console.log( response ? "S" : "N")

}

main();