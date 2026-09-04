const input = `6 5 3 2 1`

//const input = require('fs').readFileSync("/dev/stdin", "utf8");
const lines = input.split(' ').map(element => Number(element));

function main(): void {

    let increasingly = [...lines].sort((a, b) => a - b)
    let decreasingly = [...lines].sort((a, b) => b - a)

    let C = 0, D = 0;

    for(const n in lines){
        if(lines[n] === increasingly[n]) C++
        if(lines[n] === decreasingly[n]) D++
    }

    if(C === lines.length){
        console.log('C')

    } else if (D === lines.length){
        console.log('D')

    } else {
        console.log('N')
    }

}

main();