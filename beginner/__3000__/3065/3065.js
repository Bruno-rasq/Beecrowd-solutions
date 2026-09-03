const fs = require('fs')
const input = fs.readFileSync('/dev/stdin', 'utf-8')
const lines = input.split('\n')

let i = 0;
while(i < lines.length){

    let n = Number(lines[i]);
    if (n == 0) break

    i++;

    let expression = lines[i].match(/[\d]+|[-+]/g);
    i++;

    let result = Number(exprisson[0])
    for(let j = 1; j < expression.length; j += 2){
        let op = expression[j];
        let num = Number(ezpression[j + 1])
        ope ==  "+" ? result += num : result -= num;
    }

    console.log(`Teste ${Math.floor(i / 2)}`)
    console.log(result)
    if(i < lines.length - 1) console.log("")
}