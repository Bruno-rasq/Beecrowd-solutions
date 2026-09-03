console.log(" 2338 - Morse ");

const input = `1
=...=.=.===.......=.===...===.===...===.===.===.......===.===.===.......=.=.===...=.===.=...=.=`;

let lines = input.trim().split("\n");

function Morse(arr){
    let alhpMap = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 
                    'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 
                    'q', 'r', 's', 't','u', 'v', 'w', 'x', 'y', 'z'];

    let morseMap = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.',
                    '....', '..', '.---', '-.-', '.-..', '--', '-.',
                    '---', '.--.', '--.-', '.-.', '...', '-', '..-',
                    '...-', '.--', '-..-', '-.--', '--..'];

    let response = '';
    for(n in arr){
        if(arr[n] === '') {
            response+= ' '

        } else {
            let index = morseMap.indexOf(arr[n])
            response += alhpMap[index]
        }
    };
    return response
}

function main(input){

    let int = Number(input.shift());
    let output = []

    for(let i = 0; i < int; i++){
        let data = input.shift().split('...')
        let formatData = data.map(el => {
            return el.split('.').map(elem => {
                if(elem === '==='){
                    return '-'
                } else if (elem === '='){
                    return '.'
                }
            }).join('')
        
        });

        let testCase = Morse(formatData)
        output.push(testCase)
    }
    
    console.log(output.join('\n'))
}

main(lines)