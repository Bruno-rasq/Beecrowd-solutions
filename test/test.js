// let input = require('fs').readFileSync("./test/stdin", 'utf8');
// let lines = input.split('\n');

console.log(" 1768 -  ");

const input = `9
5`;

let lines = input.split('\n');

for(let i = 0; i < lines.length; i++){

    let widthTree = Number(lines[i])
    let heightTree = Math.round(widthTree/2)

    //Insert your code here.
    
}

function TreeRoot(width){

    let root = ['*', '*', '*'];
    let branch = ['*'];

    while(root.length < width){
        root.unshift(' ')
        root.push(' ')
    }

    while(branch.length < width){
        branch.unshift(' ')
        branch.push(' ')
    }

    let arr = [branch.join(' '), root.join(' ')]

    return arr.join('\n')
}