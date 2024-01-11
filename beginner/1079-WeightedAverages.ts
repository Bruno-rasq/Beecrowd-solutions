const input = `3
6.5 4.3 6.2
5.1 4.2 8.1
8.0 9.0 10.0`;

// const input = require('fs').readFileSync('/dev/stdin', 'utf8');
const lines = input.split('\n')

Output(lines)

function weightedAverage(weights: number[]): string {
    let [p1, p2, p3] = weights
    return (((p1 * 2) + (p2 * 3)+ (p3 * 5)) / 10).toFixed(1)
}

function Output(datas: string[]): void {

    let int = Number(datas.shift())

    for(let i = 0; i < int; i++){
        console.log(weightedAverage(datas[i].split(' ').map(el => Number(el))))
    }
}