console.log(" 1024 - Encryption ");


const input = `4
Texto #3
abcABC1
vxpdylY .ph
vv.xwfxo.fd`;

let lines = input.split('\n');
let int = lines.shift();

for (let i = 0; i < int; i++){

    let line = lines[i].split('');

    let charCode = right(line);
    let revert = reverse(charCode).join('');
    let response = SplitAndLeft(revert);

    console.log(response);
};

function reverse(strg){
    return strg.reverse();
};

function right(char){

    let code = char.map(element => {
        return element.charCodeAt();
    });

    let right = code.map(item => {
        if(item >= 65 && item <= 90 || item >= 97 && item <= 122){
            return item + 3;
        } else {
            return item
        }
    });

    let response = right.map(i => {
        return String.fromCharCode(i);
    })

    return response;
};

function SplitAndLeft(str){
    
    let metade = Math.round(str.length / 2);

    let part1 = str.slice(0, metade -1);
    let part2 = str.slice(metade).split('');

    let codePart2 = part2.map(e => {
        return e.charCodeAt();
    });

    let left = codePart2.map(item => {
        return item - 1;
    });

    let charCode2 = left.map(i => {
        return String.fromCharCode(i);
    });

    let response = part1 + charCode2.join('');

    return response;
};


