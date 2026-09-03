const input = `3
spock spock
tesoura spock
lagarto spock`

const lines = input.split('\n')

// const input = require('fs').readFileSync('/dev/stdin', 'utf8');
// const lines = input.split('\n')


type SelectGame =  "pedra" | "papel" | "tesoura" | "lagarto" | "spock" 

const log = (arg: any) => console.log(arg)

const rock_paper_scissor_lizard_spock = (rajesh: SelectGame, sheldon: SelectGame): void => {

    enum typesSelect {
        pedra = 0,
        papel = 1,
        tesoura = 2,
        lagarto = 3,
        spock = 4
    }

    const select = [
        ['tesoura', 'lagarto'], // pedra,
        ['pedra', 'spock'],     // papel,
        ['papel', 'lagarto'],   // tesoura,
        ['spock', 'papel'],     // lagarto,
        ['tesoura', 'pedra'],   // spock
    ]

    select[typesSelect[rajesh]].includes(sheldon) ? log('rajesh') : log('sheldon')

}

const main = (data: string[]): void => {

    let int = Number(data.shift())

    for (let i = 0; i < int; i++) {
        let [ r, s ] = data[i].split(' ')

        r === s ? console.log("empate") : rock_paper_scissor_lizard_spock(r as SelectGame , s as SelectGame)
    }
}

main(lines)