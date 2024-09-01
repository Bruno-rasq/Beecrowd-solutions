console.log(" 1024 - encryption ");

/*
    PSEUDOCODIGO:
        -pegar cada caso de teste
        -dividir os caracteres da string teste.

        - mover cada caracter 3 posições p/ direita no alfabeto ASCII
            OBS: [0-9], espaço e alguns caracteres não mudam.
        - inverter a ordem dos caracteres da string.

        - dividir a string na metade
            OBS:se não for possivel dividir em partes de tamanho igual
            divida na metade e pegue a parte de maior tamanho
        - troque os caracteres da parte de maior tamanho 1 posição p/ esquerda no alf ASCII

*/

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
};

// divide a string reversa em duas partes 
// e move os caractres da segunda parte 1 posição para a esquerda
function SplitAndLeft(str){
    
    let metade = Math.round(str.length / 2);

    let part1 = str.slice(0, metade -1).split('');
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

    let response = part1.join('') + charCode2.join('');

    return response;
};