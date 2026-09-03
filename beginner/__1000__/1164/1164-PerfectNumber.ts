const fs = require("fs")
const input = fs.readFileSync('/dev/stdin', 'utf-8')
const lines = input.split('\n').map(Number)

function isPerfect(num: number): string {

    let result: number = 0;
    for(let i = 1; i < num; i++){
        if(num % i === 0) result += i
    }

    let response = `${num} nao eh perfeito`
    if(num === result){
        response = `${num} eh perfeito`
    }
    return response 
}

function main(){
    let int = lines.shift()
    for(let i = 0; i< int; i++){
        let curr = lines[i]
        console.log(isPerfect(curr))
    }
}

main()