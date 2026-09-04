const fs = require("fs")
const input = fs.readFileSync("/dev/stdin", "utf8").split(" ").map(Number)

const quickSort = (arr) => {
    if(arr.length <= 1) return arr;
    
    let pivo = arr[Math.floor(arr.length / 2)]
    let left = []
    let right = []
    let middle = []
    for (const value of arr) {
        if (value < pivo) left.push(value);
        if (value > pivo) right.push(value);
        if (value == pivo) middle.push(value);
    }
    
    return [...quickSort(left), ...middle, ...quickSort(right)]
}

const pontuacoes = quickSort(input)
console.log(pontuacoes[1])