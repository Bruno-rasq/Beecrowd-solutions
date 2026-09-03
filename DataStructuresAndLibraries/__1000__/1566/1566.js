const fs = require("fs")
const input = fs.readFileSync("/dev/stdin", "utf8").trim().split('\n')

const countingSort = (v, limite) => {
    let aux = Array(limite).fill(0)

    for(let i = 0; i < v.length; i++){
        aux[v[i]] += 1;
    }

    let k = 0;
    for(let i = 0; i < limite; i++){
        for(let j = 0; j < aux[i]; j++){
            v[k++] = i;
        }
    }
}

let nc = Number(input.shift())
for(let i = 0; i < nc; i++){
    let curr = Number(input.shift())
    let list = input.shift().split(' ').map(Number)

    countingSort(list, 231)
    console.log(list.join(' '))
}