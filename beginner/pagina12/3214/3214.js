const fs = require('fs')
const input = fs.readFileSync('/dev/stdin' , 'utf-8')
const lines = input.split(' ').map(Number)

let [E, G, F] = lines
let count = 0

 E += G

 while(E >= F){
    /**
     * E = vazia
     * G ganha por dia
     * F = quantidade para troca
     */

    E = (E - F + 1);
    count++
 }

 console.log(count)