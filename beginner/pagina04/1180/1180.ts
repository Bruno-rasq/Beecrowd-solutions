const input_1180 = `10
1 2 3 4 -5 6 7 8 9 10`

//const fs = require('fs')
//const input = fs.readFileSync('/dev/stdin', 'utf-8')
const lines_1180 = input_1180.split("\n")

let len = Number(lines_1180.shift())
let data = String(lines_1180).split(" ").map(Number)

const lowest = (
  len: number,
  data: number[]
) => {
  let min = data.shift()
  let pos = 0
  for(let i=0; i<len - 1; i++){
    if(data[i] < min){
      min = data[i]
      pos = i
    }
  }
  console.log(`Menor valor: ${min}`)
  console.log(`Posicao: ${pos + 1}`)
}

lowest(len, data)