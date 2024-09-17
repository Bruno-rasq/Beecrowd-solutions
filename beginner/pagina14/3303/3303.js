const fs = require('fs')
const input = fs.readFileSync('/dev/stdin', 'utf-8')

console.log(input.length >= 10 ? 'palavrao' : 'palavrinha')