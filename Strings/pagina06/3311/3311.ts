const fs = require("fs")
const input = fs.readFileSync("/dev/stdin", "utf8")

const lines = input.split('\n')
const number_of_names = Number(lines.shift())

const sorted_names = lines.sort((a, b) => {
    if(a[0] === b[0]){ return 0;}
    return a[0].localeCompare(b[0])
});

for(let i = 0; i < number_of_names; i++){
    console.log(sorted_names[i])
}