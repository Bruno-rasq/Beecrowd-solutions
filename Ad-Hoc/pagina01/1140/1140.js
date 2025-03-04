const fs = require("fs");
const input = fs.readFileSync("/dev/stdin", "utf8").split("\n");

const IsTautogram = (phrase) => {

   let firstChars = phrase.map((word) => {
        let aux = word.toLowerCase().split('')
        return aux[0]
   })

   let initialChar = firstChars.shift()

   let response = firstChars.every(
       (char) => char == initialChar 
    )

   console.log(response ? 'Y' : 'N')
}

for(let i = 0; i < input.length; i++){
    let data = input[i]
    if(data == '*') break
    IsTautogram(data.split(' '))
}