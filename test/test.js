console.log(" 1024 - Encryption ");


const input = `4
Texto #3
abcABC1
vxpdylY .ph
vv.xwfxo.fd`;

let lines = input.split('\n');
let int = lines.shift();


console.log(lines);

for (let i = 0; i < int; i++){

    let line = lines[i].split('');

    let charCode = right(line);
    let revert = reverse(charCode);

    console.log(revert);
};


// inverte a ordem da string
function reverse(strg){
    return strg.reverse();
};


// move cada caracter 3 posições para direita
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
}
