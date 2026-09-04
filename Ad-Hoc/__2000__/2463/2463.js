const fs = require("fs")
const input = fs.readFileSync("/dev/stdin", "utf8").split("\n")
const [n , salas] = input
const arr = salas.split(' ').map(Number)

const Kadane_algorithm = () => {

    let local_max = arr[0];
    let global_max = arr[0];

    for(let i= 1; i < Number(n); i++){
        local_max = Math.max(arr[i], local_max + arr[i])
        if(local_max > global_max){
            global_max = local_max
        }
    }

    console.log(global_max)
}

Kadane_algorithm()