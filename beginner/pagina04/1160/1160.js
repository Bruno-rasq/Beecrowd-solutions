const fs = require('fs')
const input = fs.readFileSync('/dev/stdin', 'utf-8')
const lines = input.split('\n')

const number_of_test_cases = Number(lines.shift())
const test_cases = lines.map(testcase => testcase.split(' ').map(Number))


const population_increase = (PA, PB, GA, GB) => {

    let response = 1;
    for(let anos = 1; PA <= PB && anos < 101; ++anos){
        PA += Math.floor(PA * GA)
        PB += Math.floor(PB * GB)
        response++
    }

    return PA <= PB ? "Mais de 1 seculo." : `${response - 1} anos.`
}

const main = () => {
    for(let i = 0; i < number_of_test_cases; i++){
        let PA = test_cases[i][0]
        let PB = test_cases[i][1]
        let GA = test_cases[i][2] / 100
        let GB = test_cases[i][3] / 100

        let result = population_increase( PA, PB, GA, GB )

        console.log(result)
    }
}

main()