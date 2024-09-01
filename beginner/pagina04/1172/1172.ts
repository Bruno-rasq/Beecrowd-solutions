const input_1172 = `0
-6
63
0
0
5
-8
3
-2
7`

//const fs = require('fs')
//const input = fs.readFileSync('/dev/stdin', 'utf-8')
const lines_1172 = input_1172.split('\n').map(Number)

for(let i = 0; i < 10; i++){
  let curr_1172 = lines_1172[i]

  let result = `X[${i}] = ${ curr_1172 <= 0 ? 1 : curr_1172}`
  console.log(result)
}