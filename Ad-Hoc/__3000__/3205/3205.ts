const input: string[] = require('fs').readFileSync('/dev/stdin', 'utf8').trim().split('\n');
const testCases: number = Number(input.shift());

for(let i = 0; i < testCases; i++){
    let [r, e, c] = input.shift().split(' ').map(Number);
    let profitAdvertise: number = e - c;
    let ans: string = "does not matter";
    
    if (profitAdvertise > r)        ans = "advertise"
    else if (profitAdvertise < r)   ans = "do not advertise"
    console.log(ans)
}