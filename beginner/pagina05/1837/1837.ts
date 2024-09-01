const input_1837 =`-7 3`

//const fs = require('fs')
//const input = fs.readFileSync('/dev/stdin', 'utf-8')
const [a, b] = input_1837.split(" ").map(Number)

function calcular(x: number, y: number){
  let quo = 0

  if((x > 0 && y > 0) || (x < 0 && y > 0)){
    quo = Math.floor(x/b)
  } else {
    quo = Math.ceil(x/b)
  }

  console.log(`${quo} ${x - (y * quo)}`)
}

calcular(a, b)