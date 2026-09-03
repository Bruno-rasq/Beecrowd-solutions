const input_1914 = `4
Quico PAR Chiquinha IMPAR
9 7
Dami PAR Marcus IMPAR
12 3
Dayran PAR Conrado IMPAR
3 1000000000
Popis PAR Chaves IMPAR
2 7`

// const fs = require('fs')
// const input = fs.readFileSync('/dev/stdin', 'utf-8')
const lines_1914 = input_1914.split('\n')

const loop = Number(lines_1914.shift())

for(let i = 0; i < loop; i++){
  let [p1, j1, p2, j2] = String(lines_1914.shift()).split(' ')
  let [n1, n2] = String(lines_1914.shift()).split(' ').map(Number)

  let result = (n1 + n2) % 2 == 0 ? 'PAR' : 'IMPAR';

  if( result == j1) console.log(p1)
  if( result == j2) console.log(p2)
}