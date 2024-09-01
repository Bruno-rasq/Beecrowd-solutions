const input_1028 =`3
8 12
9 27
259 111`

//const fs = require('fs')
//const input = fs.readFileSync('/dev/stdin', 'utf-8')
const lines_1028 = input_1028.split("\n")


const MDC = (a: number, b: number): number => {
  return (b === 0) ? a : MDC(b, a % b);
}

const main_1028 = (arr: string[]): void => {
  const testcases = Number(arr.shift())
  for(let i = 0; i < testcases; i++){
    
    let [ R, V ] = arr[i].split(" ").map(Number)
    console.log(
      MDC(R, V)
    )
  }
} // OK

console.time('benchmark')
main_1028(lines_1028)
console.timeEnd('benchmark')