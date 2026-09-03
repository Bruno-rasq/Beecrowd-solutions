const input = `34
56
44
23
-2`
const lines = input.split('\n')

// const input = require('fs').readFileSync('/dev/stdin', 'utf8');
// const lines = input.split('\n')

const Ages = (ages: string[]): void => {
    
    let int = 0
    let count = 0
    let sum = 0

    while(int < ages.length){
        let curr = Number(ages[int])
        if(curr > 0){
            sum += curr
            count++
        }
        int++
    }
    console.log((sum / count).toFixed(2))
}

Ages(lines)