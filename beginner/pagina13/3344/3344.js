const fs = require("fs")
const input = fs.readFileSync('/dev/stdin', 'utf8')
let n = Number(input)

let unitarios = [
    4, 3, 3, 5, 4, 4, 3, 5, 5, 4, 3,
    6, 6, 8, 8, 7, 7, 9, 8, 8, 6
]

let decimais = [6, 6, 5, 5, 5, 7, 6, 6]

for(let i = 0; i < 1000; i++){
    if(n === 100) {n = 11}
    else if (n <= 20){ n = unitarios[n]}
    else {
        let dec = parseInt(n / 10)
        let uni = parseInt(n % 10)
        let result = decimais[dec - 2]
        if(uni !== 0){
            result += unitarios[uni]
        }
        n = result
    }
}

console.log(n)