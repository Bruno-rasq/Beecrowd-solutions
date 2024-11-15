const fs = require('fs')
const input = fs.readFileSync('/dev/stdin', 'utf-8')
const [c, n] = input.split(' ').map(Number)

type BIgORNot = bigint | number;

const Pow = (a: BIgORNot, b: BIgORNot): BIgORNot => {
    return typeof a ==  "number" && typeof b == "number" ? Math.pow(a, b) : Math.pow(a, (b as bigint));
}

const Fatorial = (n: BIgORNot): BIgORNot => {
    if(typeof n == "number"){
        if(n == 1) return n;
        let result = 1;
        for(let i = 2; i <= n; i++){
            result *= i;
        }
        return result;
    } else {
        if(n === 1n) return 1n;
        let result = 1n;
        for(let i = 2n; i <= n; i++){
            result *= i;
        }
        return result; 
    }
}

function desafioA(c: number, n: number){
    let pow = Pow(c, n);
    let fatorial = Fatorial(n);

    return pow > fatorial ? 0 : 1
}

console.log(desafioA(c, n));
