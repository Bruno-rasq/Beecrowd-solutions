const input = `5
4A5
3A3
4f2
2G4
7Z1`

const lines = input.split('\n')

// const input = require('fs').readFileSync('/dev/stdin', 'utf8');
// const lines = input.split('\n')

/**
 * @description função que exibi no console o resultado do jogo de Paula
 * @params {number} dig1   - primeiro digito
 * @params {string} letter - caracter
 * @params {number} dig2   - segundo digito
 * @retuns {void}
 */

const paulas_mathematics_game = (dig1: number, letter: string, dig2: number): void => {

    if(dig1 === dig2){
        console.log(dig1 * dig2)

    } else {

        let letter_aux = letter.toUpperCase()

        letter === letter_aux 
        ? console.log(dig2 - dig1) 
        : console.log(dig2 + dig1)

    }
}

function main() : void  {

    let int = Number(lines.shift())

    for(let i = 0; i < int; i++){

        let [ D1, L, D2 ] = lines[i].split('')

       paulas_mathematics_game(Number(D1), L, Number(D2))
    }
    
}

main()