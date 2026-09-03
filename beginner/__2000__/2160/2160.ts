const input = require('fs').readFileSync('/dev/stdin', 'utf-8')

if(input.length <= 81){
    console.log("YES")
} else {
    console.log("NO")
}