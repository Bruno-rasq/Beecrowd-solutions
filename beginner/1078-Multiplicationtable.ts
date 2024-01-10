const input = '140';
// const input = require('fs').readFileSync('/dev/stdin', 'utf8');
const MultiplyTable = (num: number): void => {
    for(let i = 1; i <= 10; i++){
        console.log(`${i} x ${num} = ${num * i}`)
    }
}
  
MultiplyTable(Number(input))