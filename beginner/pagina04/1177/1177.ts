const input_1177 = `3`

//const fs = require('fs')
//const input = fs.readFileSync('/dev/stdin', 'utf-8')
const lines_1177 = input_1177.split('\n').map(Number)
const loop = lines_1177[0]

let T = 0
let limit = 15
while(T < limit){
  for(let i = 0; i < loop; i++){
    if(T < limit){
      console.log(`N[${T++}] = ${i}`)  
    }
  }
}