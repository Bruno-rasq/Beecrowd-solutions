const input = `3
40.0
200.0
300.0`

const lines = input.split('\n')

// const input = require('fs').readFileSync('/dev/stdin', 'utf8');
// const lines = input.split('\n')

const how_many_days = (foodInKg: number) => {

    let days = 0;
    let aux = foodInKg

    while(aux > 1){
        days++
        aux = aux / 2
    }

    console.log(`${days} dias`)
}

function main() {

    let int = Number(lines.shift())
    for(let i = 0; i < int; i++){

        let food_in_kg = Number(lines[i])

        how_many_days(food_in_kg)
    }
}

main()