console.log(" 1253 - Caesar Cipher ");

const input = `6
VQREQFGT
2
ABCDEFGHIJKLMNOPQRSTUVWXYZ
10
TOPCODER
0
ZWBGLZ
25
DBNPCBQ
1
LIPPSASVPH
4`;

let lines = input.split('\n');
let int = Number(lines.shift());

let T = 0
while(T < int){

    let word = lines.shift().trim().toLowerCase();
    let key = Number(lines.shift());

    let output = CaesarCipher(word, key)

    console.log(output)

    T++
}

function CaesarCipher(strg, key){

    let alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 
                    'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 
                    'q', 'r', 's', 't','u', 'v', 'w', 'x', 'y', 'z'];

    let arr = strg.split('');

    let response = arr.map(letter => {
        let pos = alphabet.indexOf(letter)
        let ind = (pos - key) < 0 ? ((pos - key + 26) % 26) : (pos - key) % 26

        return alphabet[ind]
    }).join('');

    return response.toUpperCase();
};