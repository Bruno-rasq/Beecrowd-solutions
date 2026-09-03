const input_1175 = `0
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
const lines_1175 = input_1175.split('\n').map(Number)

for(let i = 0; i < 10; i++){
  let curr_1175 = lines_1175[lines_1175.length - i - 1]

  let result = `N[${i}] = ${curr_1175}`
  console.log(result)
}