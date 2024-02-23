const input = `hahah`

// const input = require('fs').readFileSync('/dev/stdin', 'utf8')
const lines = input.trim().split('')

/**
 * @description verifica a qualidade da risada com base na ordem das vogais
 * @param {string}  - array dos caracteres que formam a string
 * @retuns {string} returna S se a qualidade for boa ou N se não.
 */

const huahuahua = (strg: string[]): void => {

    let vowels = []
    let rev_vowels: string[] = []

    for(let i = 0; i < strg.length; i++){
        if(/[aeuio]/i.test(strg[i])){
            vowels.push(strg[i])
        }
    }

    rev_vowels = [...vowels].reverse()

    console.log(vowels.join('') === rev_vowels.join('') ? 'S' : 'N')
}

 huahuahua(lines)