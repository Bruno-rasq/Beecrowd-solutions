const input = `6
100 150 1.0 0
90000 120000 5.5 3.5
56700 72000 5.2 3.0
123 2000 3.0 2.0
100000 110000 1.5 0.5
62422 484317 3.1 1.0`

//const fs = require('fs')
//const input = fs.readFileSync('/dev/stdin', 'utf-8')
const lines = input.split('\n')

const number_of_test_cases = Number(lines.shift())
const test_cases = lines.map(testcase => testcase.split(' ').map(Number))

type DATA = {
    PA: number, // população inicial A
    PB: number, // população inicial B
    GA: number, // crescimento populacional A
    GB: number, // crescimento populacional B
}

const population_increase = (params: DATA): string => {
    let { PA, PB, GA, GB } = params

    let response = 1;
    for(let anos = 1; PA <= PB && anos < 101; ++anos){
        PA += Math.floor(PA * GA)
        PB += Math.floor(PB * GB)
        response++
    }

    return PA <= PB ? "Mais de 1 seculo." : `${response - 1} anos.`
}

const main = (): void => {
    for(let i = 0; i < number_of_test_cases; i++){
        let PA = test_cases[i][0]
        let PB = test_cases[i][1]
        let GA = test_cases[i][2] / 100
        let GB = test_cases[i][3] / 100

        let result = population_increase({ PA, PB, GA, GB })

        console.log(result)
    }
}

main()