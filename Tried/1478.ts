
const input_1487 = `9
10
0`

//const fs = require('fs')
//const input = fs.readFileSync('/dev/stdin', 'utf-8')
const lines_1487 = input_1487.split('\n').map(Number)

function next_1487 () {
  return Number(lines_1487.shift())
}


function matrix_1487(n: number) {
  let list = Array.from({ length: n }, (_, i) => i + 1);
  const maxDigits = String(n).length; // 
  const spacing = 3;

  for (let i = 0; i < n; i++) {
    
    let output = list.map(num => {
      return String(num).padStart(maxDigits)
    }).join(' '.repeat(spacing - maxDigits + 1));
    
    console.log(output);
    list.pop();
    list.unshift(i + 2);
  }
}

let curr = next_1487()
while(curr != 0 ){
  matrix_1487(curr)
  curr = next_1487()
  if(curr != 0 ){
    console.log('')
  }
}